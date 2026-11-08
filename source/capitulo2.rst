====================================================
Primeros programas
====================================================

Encendiendo un led
====================
Nuestra primera práctica consistirá en el típico **Hola Mundo** electrónico. Encenderemos/apagaremos un diodo led.
En la siguiente figura puedes ver cómo debes conectar el diodo con su resistencia a la ESP32 antes de programarla.
Puedes hacer click con el botón derecho del ratón en la imagen para poder verla más grande.

El esquema
-------------

.. warning:: El **ánodo** del diodo led está conectado, a través de una resistencia, al **GPIO26** de la placa mientras que el **cátodo** se encuentra conectado al **GND** de la placa a través de una de las líneas de alimentación.

.. container:: imagen-separada

    .. image:: /_static/capitulo2/ESP32-Led.png
        :alt: Detalle de la placa
        :align: center
        :width: 90%

En el caso de que dispongamos de elementos de la marca KeyStudio podríamos montar el circuito de esta manera. Si observas verás que usamos un cable extra, es para proporcionar corriente al led, conectado al pin **5v**. Además ya no usamos una resistencia para proteger al led porque viene incorporada en la propia PCB de KeyStudio, esto está bien pero nos quita libertad a la hora de diseñar nuestros propios circuitos.

.. container:: imagen-separada

    .. image:: /_static/capitulo2/LED_KeyStudio.png
        :alt: Detalle de la placa
        :align: center
        :width: 90%

El programa
-------------

.. note:: Este programa no lo vamos a descargar en la placa. La tendremos conectada y pulsaremos el 
    botón **Ejecutar** de Thonny para probarlo. El diodo led se encenderá/apagará según el intervalo de 
    tiempo que hayamos establecido con la función **sleep_ms()**.

.. literalinclude:: programas/capitulo2/ejer01.py
    :language: python
    :linenos:

.. rubric:: Puedes descargarte el archivo:
    :download:`Descarga el archivo <programas/capitulo2/ejer01.py>`

-----

Posibles mejoras del código
----------------------------

Veamos ahora dos variantes del mismo programa.

En esta primera variante no nos importa conocer si el led está encendido o no, simplemente le indicamos que su valor debe ser el contrario (de ahí el operador **not**) al que tenía.

.. code-block:: python
   :linenos:

   while True:
    led.value(not led.value())
    sleep_ms(100)
    led.value(not led.value())
    sleep_ms(100)

Ya en esta variante el código se reduce al máximo gracias a la función **toggle()**. Ella misma se encarga de cambiar el estado del diodo led según el tiempo que le hayamos indicado sin que tengamos que hacer nada.

.. code-block:: python
   :linenos:

    while True:
        led.toggle()
        sleep_ms(500)



Usando un pulsador
====================

El pulsador o botón es el dispositivo que permite el paso de intensidad cuando es pulsado. Una vez se deja de presionar vuelve a su posición inicial. 

Está formado por cuatro patas o terminales, conectados “dos a dos” como se observa a continuación:

.. container:: imagen-separada

    .. figure:: /_static/capitulo2/img_pulsador.png
        :width: 90%
        :align: center

        **Fuente:** `<https://inputmakers.com/>`_

El esquema
-------------

Asegúrate de conectar bien los cables. Si es necesario haz click en la imagen para verla más grande.

.. container:: imagen-separada

    .. image:: /_static/capitulo2/ESP32-Pulsador.png
        :align: center
        :width: 90%

El siguiente esquema usa el componente **botón de KeyStudio**:

.. container:: imagen-separada

    .. image:: /_static/capitulo2/Btn_Keystudio.png
        :align: center
        :width: 90%

El programa
-------------

.. literalinclude:: programas/capitulo2/ejer02.py
    :language: python
    :linenos:

.. rubric:: Puedes descargarte el archivo:
    :download:`Descarga el archivo <programas/capitulo2/ejer02.py>`

Si te fijas en el programa, las **líneas 28 y 29** las usamos para obtener el valor (estado) del pulsador y mostrar ese dato en la consola de Thonny.

Podemos mejorar el programa haciendo que en la consola, en lugar de 0 y 1 muestre un texto indicando si el led está encendido o apagado. Para ello nos valdremos de dos variables auxiliares donde guardaremos el **estado_actual** y **estado_anterior** del led, de tal manera que si el programa detecta una diferencia entre sus valores significará que el botón ha sido pulsado y solo habrá que indicar cómo se encuentra el led:

.. code-block:: python
   :linenos:

    from machine import Pin
    from time import sleep_ms
    
    GPIO_LED = 26	#D2
    GPIO_BOTON = 25 #D3
    
    led = Pin(GPIO_LED, Pin.OUT, value=0)
    boton = Pin(GPIO_BOTON, Pin.IN, Pin.PULL_UP)

    estado_anterior = -1

    while True:
        estado_actual = boton.value()
        
        if estado_actual == 0:
            led.value(1)
        else:
            led.value(0)
        
        if estado_actual != estado_anterior:
            if estado_actual == 0:
                print("Botón PULSADO: LED ON")
            else:
                print("Botón LIBERADO: LED OFF")
            estado_antarior = estado_actual
        sleep_ms(50)    

