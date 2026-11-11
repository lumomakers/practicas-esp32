Módulo Time
========================
El módulo `time` permite introducir pausas, medir intervalos y organizar acciones periódicas. En robótica sirve para decidir **cuándo** actuar y **durante cuánto tiempo**.

¿Para qué sirve?
---------------------

- Encender un LED durante dos segundos.
- Hacer avanzar un robot durante un intervalo.
- Consultar sensores cada 100 milisegundos.
- Medir la duración de una operación.
- Ejecutar tareas periódicas sin detener el programa.

En algunas versiones de MicroPython también se encuentra el módulo `utime`.

Importar el módulo
----------------------
.. code-block:: python

    import time
    time.sleep(2)


También podemos importar funciones concretas:

.. code-block:: python

    from time import sleep, ticks_ms, ticks_diff
    sleep(2)

Funciones principales
-----------------------
.. list-table:: 
   :header-rows: 1
   :widths: 30 40

   * - Función
     - Utilidad
   * - `sleep(s)`
     - Pausa en segundos 
   * - `sleep_ms(ms)`
     - Pausa en milisegundos
   * - `sleep_us(us)`
     - Pausa en microsegundos 
   * - `ticks_ms()` 
     - Contador de milisegundos
   * - `ticks_us()` 
     - Contador de microsegundos
   * - `ticks_cpu()`
     - Contador de alta resolución, si está disponible 
   * - `ticks_diff(a, b)`
     - Diferencia entre dos lecturas del contador
   * - `ticks_add(t, delta)` 
     - Suma un intervalo a una referencia temporal 
   * - `time()` 
     - Segundos desde la época del sistema
   * - `localtime()` 
     - Fecha y hora desglosadas 
   * - `mktime()`
     - Convierte una fecha y hora en segundos desde la época 

Ejemplos
----------
`sleep()`: hacer una pausa
~~~~~~~~~~~~~~~~~~~~~~~~~~~
.. code-block:: python

    import time

    print('Inicio')
    time.sleep(3)
    print('Han pasado 3 segundos')

Durante `sleep()` la ejecución de ese programa queda bloqueada.

LED intermitente
~~~~~~~~~~~~~~~~~
.. code-block:: python
    
    from machine import Pin
    import time

    led = Pin(15, Pin.OUT)  # GPIO ilustrativo: verificar el pinout

    while True:
        led.on()
        time.sleep(1)
        led.off()
        time.sleep(1)

El LED permanece encendido un segundo y apagado otro segundo.

`sleep_ms()` y `sleep_us()`
~~~~~~~~~~~~~~~~~~~~~~~~~~~
- 1 segundo = 1.000 milisegundos.
- 1 segundo = 1.000.000 microsegundos.

.. code-block:: python

    import time

    time.sleep_ms(200)  # 0,2 segundos
    time.sleep_us(10)   # 10 microsegundos


Parpadeo rápido
~~~~~~~~~~~~~~~~
.. code-block:: python

    from machine import Pin
    import time

    led = Pin(15, Pin.OUT)

    while True:
        led.on()
        time.sleep_ms(200)
        led.off()
        time.sleep_ms(200)

El estado del LED cambia cada 200 ms; un ciclo completo dura aproximadamente 400 ms. La duración real de las pausas puede ser algo mayor por el tiempo de ejecución.

`ticks_ms()`: medir intervalos
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
`ticks_ms()` proporciona un contador interno; **no indica la hora del día**.

.. code-block:: python

    import time

    inicio = time.ticks_ms()
    time.sleep(2)
    final = time.ticks_ms()

    duracion = time.ticks_diff(final, inicio)
    print('Duración:', duracion, 'ms')


El resultado será aproximadamente 2.000 ms.

.. note:: **¿Por qué `ticks_diff()`?:** 
    Los contadores `ticks_ms()` pueden volver a cero al alcanzar su límite. `ticks_diff()` permite calcular diferencias correctamente dentro del intervalo admitido por el contador. Por eso es preferible a restar directamente dos lecturas.

