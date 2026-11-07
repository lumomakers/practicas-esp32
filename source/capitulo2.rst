====================================================
Capítulo 2: Primeros programas
====================================================

Encendiendo un led
====================

.. literalinclude:: programas/capitulo2/ejer01.py
    :language: python
    :linenos:

.. rubric:: Archivo para el alumnado
:download:`Descarga el archivo <programas/capitulo2/ejer01.py>`

Prueba ahora a modificar el bucle while con las siguientes variantes:

.. code-block:: python
   :caption: Variante 1
   :linenos:

    while True:
        led.toggle()
        sleep_ms(500)

.. code-block:: python
   :caption: Variante 2
   :linenos:

   while True:
    led.value(not led.value())
    sleep_ms(100)
    led.value(not led.value())
    sleep_ms(100)


