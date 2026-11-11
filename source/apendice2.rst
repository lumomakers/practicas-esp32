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
`sleep()` : hacer una pausa
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

    led = Pin(25, Pin.OUT)  # GPIO ilustrativo: verificar el pinout

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

    led = Pin(25, Pin.OUT)

    while True:
        led.on()
        time.sleep_ms(200)
        led.off()
        time.sleep_ms(200)

El estado del LED cambia cada 200 ms; un ciclo completo dura aproximadamente 400 ms. La duración real de las pausas puede ser algo mayor por el tiempo de ejecución.

`ticks_ms()` : medir intervalos
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

.. note:: **¿Por qué ticks_diff()?:** 
    Los contadores `ticks_ms()` pueden volver a cero al alcanzar su límite. `ticks_diff()` permite calcular diferencias correctamente dentro del intervalo admitido por el contador. Por eso es preferible a restar directamente dos lecturas.

Parpadeo sin bloquear el programa
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
.. code-block:: python

    from machine import Pin
    import time

    led = Pin(25, Pin.OUT)
    anterior = time.ticks_ms()
    intervalo = 500

    while True:
        ahora = time.ticks_ms()

        if time.ticks_diff(ahora, anterior) >= intervalo:
            led.toggle()
            anterior = ahora
        # Aquí podemos consultar sensores u otras entradas.

.. tip:: **Funcionamiento:** guardamos una referencia temporal, consultamos el contador y cambiamos el estado del LED cuando hayan transcurrido 500 ms. Mientras tanto, el programa puede atender otras tareas.

Comparación
-------------
.. list-table:: 
   :header-rows: 1
   :widths: 30 40

   * - `sleep()`
     - `ticks_ms()` con `ticks_diff()`
   * - Introduce una pausa bloqueante
     - Permite comprobar el tiempo sin bloquear
   * - Es sencillo para secuencias lineales 
     - Es adecuado para tareas concurrentes en un bucle
   * - Puede retrasar la lectura de sensores  
     - Facilita la consulta frecuente de sensores

`ticks_us()` : medir operaciones rápidas
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
.. code-block:: python

    import time

    inicio = time.ticks_us()

    for i in range(100):
        resultado = i * i

    final = time.ticks_us()
    print('Tiempo:', time.ticks_diff(final, inicio), 'microsegundos')


.. note:: **ticks_cpu()** (sin el espacio inicial al escribirlo en código) también puede existir, pero su disponibilidad y unidad dependen del puerto de MicroPython.

`time()` y `localtime()` : fechas y horas
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
.. code-block:: python

    import time

    print(time.time())
    print(time.localtime())

    fecha = time.localtime()
    print('Año:', fecha[0])
    print('Mes:', fecha[1])
    print('Día:', fecha[2])
    print('Hora:', fecha[3])
    print('Minuto:', fecha[4])


.. note:: **time.time()** devuelve segundos desde la época del sistema, que depende del puerto y la versión. **localtime()** devuelve una tupla con la fecha y hora. **La fecha y hora solo serán fiables si el reloj está configurado o sincronizado**.

Errores frecuentes
---------------------
.. list-table:: 
   :header-rows: 1
   :widths: 30 40

   * - Error
     - Corrección
   * - **sleep(500)** para esperar medio segundo 
     - Utiliza **sleep_ms(500)**
   * - Restar directamente lecturas de `ticks_ms()` 
     - Utiliza **ticks_diff()**
   * - Interpretar **ticks_ms()** como hora actual
     - Es un contador de intervalos
   * - Abusar de pausas largas en robots autónomos 
     - Usa temporización no bloqueante 
   * - Suponer que **localtime()** siempre es correcto 
     - Configura o sincroniza el reloj


Resumen
---------
.. list-table:: 
   :header-rows: 1
   :widths: 30 40

   * - Necesidad
     - Función
   * - Esperar 2 segundos
     - **time.sleep(2)**
   * - Esperar 100 ms
     - **time.sleep_ms(100)**
   * - Esperar 10 µs 
     - **time.sleep_us(10)**
   * - Ejecutar tareas periódicas sin bloquear 
     - **ticks_ms()** + **ticks_diff()**
   * - Consultar fecha y hora
     - **time.localtime()**
   * - Obtener marca temporal en segundos
     - **time.time()**
