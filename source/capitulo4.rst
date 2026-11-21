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
Si buscas en la red observarás códigos que usan nomenclaturas del tipo **E5**, **C4**, etc. Estas etiquetas del tipo **E5** o **F5** usan el sistema de cifrado inglés (o anglosajón) acompañado del número de octava, que indica qué tan grave o aguda suena la nota.

Equivalencia de las letras (Cifrado inglés)
============================================
El cifrado inglés asigna las primeras siete letras del abecedario empezando por la nota **La**:

.. list-table:: 
   :header-rows: 1
   :widths: 30 30

   * - Cifrado inglés
     - Nota tradicional
   * - C
     - Do
   * - D
     - Re
   * - E
     - Mi
   * - F
     - Fa
   * - G
     - Sol
   * - A
     - La
   * - B
     - Si

Si aparece una almohadilla (``#``) o una ``b``, indica alteraciones: por ejemplo, **C#** es **Do sostenido** y **Bb** es **Si bemol**

¿Qué significa el número (octava)?
============================================
El número indica la **altura** (lo grave o aguda que debe ser la nota):

* **Números bajos (2,3):** notas graves (como el bajo de una canción)
* **Número 4 (C4, D4, E4...):** es la **octava central** del piano (donde está el *Do central*)
* **Número 5 (C5, D5, E5...):** una octava más aguda que la central; suele usarse en buzzers porque suena más nítida y con mejor volumen.

Por ejemplo:

* **E5** = **Mi** de la quinta octava (659 Hz)
* **F5** = **Fa** de la quinta octava (698 Hz)

¿Cómo usar nombres tradicionales en nuestro código?
======================================================
Lo ideal es tener en un diccionario las *claves* (notas) y sus *valores* (frecuencias) para escribir las melodías directamente como ``DO5``, ``RE5``, ``MI5``:

.. code-block:: python

   NOTAS = {
      "DO5": 523,
      "RE5": 587,
      "MI5": 659,
      "FA5": 698,
      "SOL5": 784,
      "LA5": 880,
      "SI5": 988,
      "SILENCIO": 0,
   }

Tabla de frecuencias (Octavas 3 a 6)
======================================
A continuación tenemos la **tabla de frecuencias (en Hz)** de la 3ª a la 6ª octava (incluyendo sostenidos ``#``).

En un buzzer pasivo, las octavas **4**, **5**, y **6** son las que mejor suenan; la octava 3 es grave y puede escucharse más baja según el modelo de buzzer.


.. list-table:: 
   :header-rows: 1
   :widths: 30 30 30 30 30 30

   * - Nota tradicional
     - Cifrado
     - Octava 3
     - Octava 4 (central)
     - Octava 5
     - Octava 6
   * - **Do**
     - C
     - 131
     - 262
     - 523
     - 1047
   * - **Do#**
     - C#
     - 139
     - 277
     - 554
     - 1109
   * - **Re**
     - D
     - 147
     - 294
     - 587
     - 1175
   * - **Re#**
     - D#
     - 156
     - 311
     - 622
     - 1245
   * - **Mi**
     - E
     - 165
     - 330
     - 659
     - 1319
   * - **Fa**
     - F
     - 175
     - 349
     - 698
     - 1397
   * - **Fa#**
     - F#
     - 185
     - 370
     - 740
     - 1480
   * - **Sol**
     - G
     - 196
     - 392
     - 784
     - 1568
   * - **Sol#**
     - G#
     - 208
     - 415
     - 831
     - 1661
   * - **La**
     - A
     - 220
     - 440
     - 880
     - 1760
   * - **La#**
     - A#
     - 233
     - 466
     - 932
     - 1865
   * - **Si**
     - B
     - 247
     - 494
     - 988
     - 1976

.. note:: Los bemoles equivalen al sostenido de la nota anterior; por ejemplo **Sib** = **La#**

Diccionario completo para tus programas en MicroPython
=======================================================

Puedes guardar el siguiente bloque en un archivo llamado ``notas.py`` en el ESP32 e importarlo en los proyectos futuros, o **pegarlo directamente en el inicio del script** con las notas que vayas a usar en tu melodía, tal y como te muestro en el ejemplo de la entrada de **Mario Bros**:

.. code-block:: python

   NOTAS = {
    # Octava 3
    "DO3": 131, "DO#3": 139, "RE3": 147, "RE#3": 156, "MI3": 165, "FA3": 175,
    "FA#3": 185, "SOL3": 196, "SOL#3": 208, "LA3": 220, "LA#3": 233, "SI3": 247,

    # Octava 4 (Central)
    "DO4": 262, "DO#4": 277, "RE4": 294, "RE#4": 311, "MI4": 330, "FA4": 349,
    "FA#4": 370, "SOL4": 392, "SOL#4": 415, "LA4": 440, "LA#4": 466, "SI4": 494,

    # Octava 5
    "DO5": 523, "DO#5": 554, "RE5": 587, "RE#5": 622, "MI5": 659, "FA5": 698,
    "FA#5": 740, "SOL5": 784, "SOL#5": 831, "LA5": 880, "LA#5": 932, "SI5": 988,

    # Octava 6
    "DO6": 1047, "DO#6": 1109, "RE6": 1175, "RE#6": 1245, "MI6": 1319, "FA6": 1397,
    "FA#6": 1480, "SOL6": 1568, "SOL#6": 1661, "LA6": 1760, "LA#6": 1865, "SI6": 1976,

    # Pausa
    "SILENCIO": 0
   }


.. rubric:: Mario Bros

.. code-block:: python

   import time
   from machine import Pin, PWM

   buzzer = PWM(Pin(17))

   # Diccionario con las notas exactas de la intro de Mario Bros
   NOTAS = {
      "SOL4": 392,
      "DO5": 523,
      "MI5": 659,
      "SOL5": 784,
      "SILENCIO": 0,
   }

   # Melodía: (Nota, duración en ms)
   mario_bros = [
      # Intro clásica
      ("MI5", 125), ("MI5", 125), ("SILENCIO", 125), ("MI5", 125),
      ("SILENCIO", 125), ("DO5", 125), ("MI5", 250),
      ("SOL5", 250), ("SILENCIO", 250), ("SOL4", 250), ("SILENCIO", 250),
   ]

   def tocar_nota(freq, duracion_ms):
      if freq == 0:
         buzzer.duty_u16(0)
         time.sleep_ms(duracion_ms)
      else:
         buzzer.freq(freq)
         buzzer.duty_u16(32768)
         time.sleep_ms(duracion_ms)
         buzzer.duty_u16(0)
         time.sleep_ms(20)  # Pausa muy corta para mantener el ritmo rápido de Mario

   for nota, duracion in mario_bros:
      tocar_nota(NOTAS[nota], duracion)

   buzzer.deinit()

