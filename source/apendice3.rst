
Cómo funcionan las señales digitales y PWM
===========================================

Señal digital: encendido y apagado
------------------------------------
Un GPIO configurado como salida puede establecer un estado lógico bajo o alto:

* ``0`` / ``LOW``: tensión próxima a 0 V.
* ``1``/ ``HIGH``: tensión próxima a 3,3 V en el ESP32.

Cuando usamos un transistor como interruptor, un nivel alto en el GPIO puede permitir el paso de corriente por el buzzer y un nivel bajo puede interrumpirlo.

.. code-block:: python

   from machine import Pin
   import time

   salida = Pin(16, Pin.OUT, value=0)
   salida.on()    # Nivel alto
   time.sleep(1)
   salida.off()   # Nivel bajo

Señal PWM: frecuencia y ciclo de trabajo
-------------------------------------------

**PWM** significa *Pulse Width Modulation* (modulación por ancho de pulsos). Permite producir una señal periódica que alterna niveles altos y bajos.

- **Frecuencia**: número de veces que se repite la señal por segundo; se expresa en hercios (Hz).
- **Ciclo de trabajo** (`duty cycle`): porcentaje de tiempo que la señal está en estado alto. Por ejemplo, un ciclo de trabajo del 50% significa que la señal está encendida la mitad del tiempo y apagada la otra mitad.

.. note:: La frecuencia PWM debe ajustarse según el dispositivo que se esté controlando. En general, una frecuencia entre 500 Hz y 1 kHz suele ser adecuada en muchos casos.

Configuración de PWM en MicroPython
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Lo primero que debemos hacer es importar el módulo ``machine`` con la clase ``PWM``. La forma general de usarlo sería:

.. code-block:: python

   from machine import PWM

   dispositivo = PWM (pin_del_dispositivo)

Algunos de los métodos de PWM que podemos usar:

.. list-table:: 
   :header-rows: 1
   :widths: 30 30

   *  - Comando
      - Descripción
   *  - ``dispositivo.freq(freq)``
      - Establece o devuelve la frecuenia de la señal PWM en hercios (Hz)
   *  - ``dispositivo.duty(duty_cycle``
      - Ajusta el ciclo de trabajo
   *  - ``dispositivo.deinit``
      - Desactiva la señal PWM en el pin del dispositivo (led, Buzzer...)
   *  - ``dispositivo.duty_u16(duty_cycle``
      - Ajusta el ciclo de trabajo con resolución de 16 bits (valor entre 0 y 65535)
   *  - ``dispositivo.init(freq, duty``
      - Inicializa el PWM con una frecuencia y un ciclo de trabajo determinados.

En el siguiente ejemplo activamos un **buzzer** conectado al GPIO17:

.. code-block:: python

   from machine import Pin, PWM

   buzzer = PWM(Pin(17))
   buzzer.freq(440)          # 440 Hz
   buzzer.duty_u16(32768)   # Aproximadamente un 50 %

Recuerda que ``duty_u16()`` acepta valores comprendidos entre **0 y 65535**. Aproximadamente:

.. list-table:: 
   :header-rows: 1
   :widths: 30 30

   *  - ``duty_u16()``
      - Ciclo de trabajo
   *  - 0
      - 0%
   *  - 16384
      - 25%         
   *  - 32768
      - 50%     
   *  - 49152
      - 75%         
   *  - 65535
      - 100%     