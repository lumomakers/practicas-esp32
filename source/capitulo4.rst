=========================
El Buzzer (o zumbador)
=========================
Un buzzer o zumbador es un pequeño dispositivo electrónico capaz de producir sonidos. En robótica podemos utilizarlo para :

- Emitir una alarma cuando un robot detecta un obstáculo.
- Avisar de que ha comenzado o terminado una operación.
- Dar señales acústicas distintas según una situación.
- Reproducir notas musicales sencillas, siempre que sea un buzzer adecuado.

El microcontrolador puede controlar un buzzer mediante señales eléctricas. La forma de control depende del **tipo de buzzer**.

¿Qué tipos de buzzer existen?
-------------------------------
Lo primero que debemos saber es que no todos los buzzers se controlan igual.


Buzzer activo y pasivo
=========================

.. container:: ficha-componente

   .. container:: ficha-foto

      .. image:: _static/capitulo4/buzzer_activo.png
         :alt: Buzzer activo

   .. container:: ficha-texto

      .. rubric:: Buzzer activo

      Un **buzzer activo** incorpora un circuito oscilador. Al aplicarle su alimentación adecuada, puede generar por sí mismo un tono de frecuencia prácticamente fija.

      - Es útil para alarmas y avisos.
      - Normalmente se controla mediante encendido y apagado.
      - En MicroPython podemos utilizar ``machine.Pin``.
      - Si requiere 5 V o consume más corriente de la que puede entregar un GPIO, necesitaremos una **etapa de control**, por ejemplo un transistor.

      Este buzzer concretamente es el **Keyestudio KS0018 – Digital Buzzer Module** y posee las siguientes características:

      .. list-table:: 
         :header-rows: 1
         :widths: 30 30

         * - Característica
           - Descripción
         * - `Tipo`
           - Activo 
         * - `Alimentación`
           - 3,3 - 5 V
         * - `Conexiones`
           - S, +, y -
         * - `MicroPython`
           - ``machine.Pin``    
         * - `Transistor adicional`
           - No es necesario, el módulo incorpora uno

      Conexión con el **ESP32 STEAMakers**:

         .. list-table:: 
            :header-rows: 1
            :widths: 30 30

            * - Keyestudio KS0018
              - STEAMakers
            * - **S** `(Señal)`
              - D5 - GPIO16 
            * - **+** `(Alimentación)`
              - 3,3 V
            * - **-** `(Tierra)`
              - GND

.. container:: ficha-componente

   .. container:: ficha-foto

      .. image:: _static/capitulo4/buzzer_pasivo.png
         :alt: Buzzer pasivo

   .. container:: ficha-texto

      .. rubric:: Buzzer pasivo

      Un **buzzer pasivo** no incorpora un oscilador que genere autónomamente la nota. Necesita una señal que cambie periódicamente.

      - Es útil para notas musicales y efectos sonoros.
      - Podemos modificar la frecuencia de la señal para cambiar de nota.
      - En MicroPython normalmente utilizamos ``machine.PWM``.
      - Según las características eléctricas del componente, puede necesitar también un transistor de control.

Comparativa
=====================
.. list-table:: 
   :header-rows: 1
   :widths: 30 30 30

   *  - Característica
      - Buzzer activo
      - Buzzer pasivo
   *  - `Oscilador interno`
      - Si
      - No 
   *  - `Sonido sostenido con alimentación continua adecuada`
      - Si
      - No
   *  - `Posibilidad de generar diferentes notas desde el programa`
      - Generalmente no
      - Si
   *  - `Control habitual`
      - ``Pin``
      - ``PWM``
   *  - `Uso habitual`
      - Avisos y alarmas
      - Notas y melodías

.. important:: **Dos terminales no significa pasivo y tres pines no significa activo**. Hay buzzers activos y pasivos de dos terminales y módulos de ambos tipos con conectores de tres pines.



¿Qué necesitamos saber sobre la ESP32 STEAMakers?
----------------------------------------------------
La ESP32 trabaja con señales GPIO de **3,3 V**. Una tensión de alimentación de 5 V en un actuador no significa que debamos aplicar 5 V a la entrada de un GPIO.

**Reglas de seguridad eléctrica:**

#. No alimentar un buzzer de **5 V** directamente desde un GPIO de **3,3 V**.
#. No dar por hecho que todos los buzzers tienen el mismo consumo.
#. Unir las masas (**GND**) del controlador y de la alimentación del actuador, cuando se utilice una etapa de control externa.
#. Verificar las patas **B**, **C** y **E** del transistor concreto: su disposición física depende de la referencia y del encapsulado.
#. No presuponer que el conector de 5 V de la placa puede alimentar cualquier carga; comprobar su capacidad de corriente y la fuente utilizada.

Ejemplos
----------

.. rubric:: Ejemplo 1: La primera nota (La4)

El siguiente código hará sonar al buzzer durante 1 segundo y luego lo desactivará al encontrar la línea de código ``buzzer.deinit()``

.. container:: imagen-separada

    .. image:: /_static/capitulo4/circuito_buzzer_01.png
        :alt: Detalle de la placa
        :align: center
        :width: 90%
      


.. code-block:: python

   from machine import Pin, PWM
   import time

   buzzer = PWM(Pin(17))
   buzzer.freq(440)          # 440 Hz
   buzzer.duty_u16(32768)   # Aproximadamente un 50 %
   time.sleep(1)
   buzzer.deinit()  

Mejoramos el código anterior:

.. code-block:: python

   from machine import Pin, PWM
   from time import sleep

   buzzer = PWM(Pin(17), freq=440, duty_u16=0)
   buzzer.duty_u16(32768)  # Señal PWM ~50%
   sleep(1)
   buzzer.duty_u16(0)      # Dejamos la salida sin pulsos
   buzzer.deinit()         # Liberamos el recurso PWM

En este caso aprovechamos la declaración de la variable ``buzzer`` para indicar en la misma instrucción la frecuencia y asegurarnos que la salida no emite nigún pulso (``duty_u16=0``).

.. note:: La frecuencia **440 Hz** corresponde a la nota **La4** (en afinación habitual). 

.. rubric:: Ejemplo 2: Distintos tonos

.. code-block:: python

   from machine import Pin, PWM
   from time import sleep

   buzzer = PWM(Pin(17), freq = 500, duty_u16=0)

   def pitido (frecuencia=1000, duracion=0.2):
      buzzer.freq(frecuencia)
      buzzer.duty_u16(32768)
      sleep(duracion)
      buzzer.duty_u16(0)

   try:
      pitido()	         # Llamada sin pasar datos
      sleep(0.2)
      pitido(500, 0.5) 	# Más grave
      sleep(0.2)
      pitido(2000, 0.1)	# Más agudo y corto
   finally:
      buzzer.deinit()


Notas musicales y melodías
---------------------------

Frecuencias aproximadas de una escala
=====================================
.. list-table:: 
   :header-rows: 1
   :widths: 30 30

   * - Nota
     - Frecuencia
   * - Do4
     - 262 Hz
   * - Re4
     - 294 MHz
   * - Mi4
     - 330 Hz
   * - Fa4
     - 349 MHz
   * - Sol4
     - 392 Hz
   * - La4
     - 440 MHz
   * - Si4
     - 494 Hz
   * - Do5
     - 523 MHz

Estas frecuencias están redondeadas a números enteros para facilitar la programación.

.. rubric:: Escala musical

.. code-block:: python

   from machine import Pin, PWM
   from time import sleep

   buzzer = PWM(Pin(17), freq=440, duty_u16=0)

   notas = [262, 294, 330, 349, 392, 440, 494, 523]

   try:
      for nota in notas:
         buzzer.freq(nota)
         buzzer.duty_u16(32768)
         sleep(0.4)
         buzzer.duty_u16(0)
         sleep(0.1)
   finally:
      buzzer.deinit()

El programa recorre una **lista de frecuencias**. Cada nota dura 0,4 segundos y queda separada por un silencia de 0,1 segundos.

.. rubric:: Notas almacenadas en un diccionario

.. code-block:: python
   from machine import Pin, PWM
   from time import sleep

   buzzer = PWM(Pin(17), freq=440, duty_u16=0)

   notas = {
      "DO": 262,
      "RE": 294,
      "MI": 330,
      "FA": 349,
      "SOL": 392,
      "LA": 440,
      "SI": 494,
      "DO5": 523,
   }

   def tocar(frecuencia, duracion):
      buzzer.freq(frecuencia)
      buzzer.duty_u16(32768)
      sleep(duracion)
      buzzer.duty_u16(0)
      sleep(0.1)

   try:
      for nombre, frecuencia in notas.items():
         print("Nota:", nombre)
         tocar(frecuencia, 0.4)
   finally:
      buzzer.deinit()

En este ejemplo usamos un **diccionario** de manera que cada nombre de nota se asocia a su frecuencia. El método ``.items()`` permite recorrer los elementos del diccionario.