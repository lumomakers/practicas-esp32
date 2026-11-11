Módulo Machine
========================

¿Qué es `machine`?
-----------------------

**machine** es un módulo de MicroPython que permite comunicarse con los componentes físicos de un microcontrolador: sus pines, conversores analógico-digitales, temporizadores y buses de comunicación.

Podemos imaginarlo como un puente entre **las instrucciones del programa** y **el hardware** (LED, pulsadores, sensores, motores y pantallas).

.. code-block:: python

    import machine

También podemos importar únicamente lo que vayamos a utilizar:

.. code-block:: python

    from machine import Pin, PWM, ADC


.. important:: La disponibilidad de clases, pines y funciones depende de la placa y de la versión o puerto de MicroPython. Los números de GPIO de los ejemplos son orientativos: consulta el pinout y el firmware de tu placa antes de conectar componentes.

Componentes principales
------------------------

.. list-table:: 
   :header-rows: 1
   :widths: 30 30 30

   * - Clase o función
     - ¿Para qué sirve?
     - Ejemplo de uso
   * - `Pin`
     - Configurar entradas y salidas digitales
     - LED y pulsador
   * - `PWM`
     - Generar señales de modulación por ancho de pulso
     - Brillo de LED o señal de servo
   * - `ADC`
     - Leer señales analógicas
     - Potenciómetro y sensor analógico
   * - `Timer`
     - Programar acciones temporizadas
     - Ejecución periódica
   * - `UART`
     - Comunicación serie
     - Comunicación con otros dispositivos
   * - `I2C`
     - Comunicación con sensores y pantallas
     - Pantalla o sensor I²C
   * - `SPI`
     - Comunicación serie síncrona
     - Pantalla o memoria SPI
   * - `RTC`
     - Acceso al reloj de tiempo real, si está disponible
     - Fecha y hora
   * - `freq()`
     - Consultar o ajustar la frecuencia de CPU, según el puerto
     - Gestión del microcontrolador
   * - `reset()`
     - Reiniciar la placa
     - Reinicio por software
   * - `unique_id()`
     - Obtener el identificador de la placa
     - Identificación de dispositivo

Tabla de consulta rápida
-------------------------

.. list-table:: 
   :header-rows: 1
   :widths: 30 30 

   * - Objetivo
     - Herramienta
   * - Encender o apagar un LED
     - Pin(..., Pin.OUT)
   * - Detectar un pulsador
     - Pin(..., Pin.IN)
   * - Leer un potenciómetro
     - ADC(...)
   * - Variar el brillo de un LED
     - PWM(...)
   * - Generar una señal de control para servo
     - PWM(...)
   * - Comunicarse por puerto serie
     - UART(...)
   * - Conectar sensores I²C
     - I2C(...)
   * - Conectar dispositivos SPI
     - SPI(...)

Ejemplo:
---------
**Pin**: encender y apagar un LED
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: python
   :linenos:

    from machine import Pin
    from time import sleep

    led = Pin(25, Pin.OUT)

    while True:
        led.value(1)
        sleep(1)
        led.value(0)
        sleep(1)

.. attention::
    - **Pin(15, Pin.OUT)** configura el GPIO 15 como salida. 
    - **value(1)** establece un nivel lógico alto.
    - **value(0)** establece un nivel lógico bajo.
    - **sleep(1)** espera un segundo.

**Nota:** Que un nivel alto encienda el LED depende de cómo esté conectado. Utiliza una resistencia limitadora adecuada con un LED externo.


