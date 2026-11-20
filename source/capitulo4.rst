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

.. rubric:: *Ejemplo 1*

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

