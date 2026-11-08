====================================================
Sensor LDR
====================================================

La fotoresistencia (LDR) pertenece a la familia de **sensores anlógicos**, es decir, aquellos que nos permiten medir magnitudes que varían suavemente: la intensidad de luz, la temperatura, la humedad del suelo, la fuerza ejercida.
La mayoría de estos sensores básicos son **Resistivos**. Esto significa que varían su resistencia eléctrica según la magnitud física, en este caso nuestra **LDR (Fotoresistencia)** cuanta **menos luz** reciba **más resistencia** ejercerá al paso de la corriente.

Para leer un LDR, no basta con conectarlo directamente al pin correspondiente (no a uno cualquiera); necesitas medir cómo cambia el valor de su resistencia. Para ello, creamos un **divisor de tensión** añadiendo una resistencia normal (generalmente de 10KΩ) y se lee la variación de voltaje resultante utilizando el convertidor analógico-digital (ADC) de la placa.

¿Y por qué? pues porque el ADC de nuestra placa solo sabe medir voltaje, no resistencia. No puedes conectar una LDR directamente entre el pin y GND. No funcionará.


.. warning::
    - **VCC (3.3V)** Patilla 1 de la LDR.
    - Punto Medio Patilla 2 de LDR + Resistencia 10k + Pin ADC.
    - **GND** El otro extremo de la resistencia 10k.

El esquema
-------------

.. container:: imagen-separada

    .. image:: /_static/capitulo3/LDR.png
        :align: center
        :width: 90%

En el caso de que dispongamos de elementos de la marca KeyStudio podríamos montar el circuito de esta manera:

.. container:: imagen-separada

    .. image:: /_static/capitulo3/LDR_KeyStudio.png
        :align: center
        :width: 90%

El programa
-------------

.. literalinclude:: programas/capitulo3/ejer03.py
    :language: python
    :linenos:

.. rubric:: Puedes descargarte el archivo:
    :download:`Descarga el archivo <programas/capitulo3/ejer03.py>`

El interruptor crepuscular
---------------------------

Vamos a unificar un par de conceptos ya adquiridos y crearemos un programa que encienda/apague un led en función de la luz recibida por la LDR (lo que viene siendo un **interruptor crepuscular**)

.. container:: imagen-separada

    .. image:: /_static/capitulo3/Interruptor_crepuscular.png
        :align: center
        :width: 90%

.. literalinclude:: programas/capitulo3/ejer03_v2.py
    :language: python
    :linenos:

.. rubric:: Puedes descargarte el archivo:
    :download:`Descarga el archivo <programas/capitulo3/ejer03_v2.py>`