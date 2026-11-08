====================================================
Nuestra placa ESP32
====================================================

¡Bienvenidos, ingenieros e ingenieras!

Hoy vamos a conocer al protagonista de todas nuestras aventuras tecnológicas: la placa de desarrollo **STEAMakers**. Esta placa tiene un superpoder oculto: lleva dentro un chip llamado **ESP32**. 

La placa `ESP32 Plus STEAMakers <https://libros.catedu.es/books/esp32-en-el-aula/page/hardware-esp32-plus-steamakers/revisions/63460/changes#:~:text=versi%C3%B3n%20de%20Innova%20Didactic>`_ nos ofrece una gran cantidad de prestaciones, entre las que destacamos:

* Wifi integrado
* Bluetooth integrado
* Puede trabajar con el código IDE de Arduino
* Zócalo para tarjetas **microSD** para almacenamiento de datos.
* Conexiones similares para shields de Arduino

También dispone de conexiones para todas las entradas y salidas con posibilidad de tener la alimentación adjunta y puertos de expansión I2C para poder conectar diferentes dispositivos directamente en la placa.

El Cerebro: El Chip ESP32
=========================

.. image:: /_static/capitulo1/placa_steamakers.png
   :alt: Detalle de la placa
   :align: center
   :width: 400px
   

La placa está basada en el microcontrolador ESP32-WROOM-32 y sus principales especificaciones técnicas son:

* Microcontrolador Tensilica Xtensa 32-bit LX6 a 160MHz.
* Conectividad WiFi 802.11 b/g/n/e/i.
* Conectividad Bluetooth 4.2 y modo BLE.
* Zócalo para tarjetas µSD.
* 14 entradas y salidas digitales con alimentación.
* Conector serie hembra con alimentación.
* Conector I2C para conectar hasta 5 dispositivos a la vez sobre la misma placa.
* Conector hembra I2C para conexión de una pantalla OLED.
* Botón de Reset.
* Conector de 5V
* Conector de 3.3V
* Interruptor 3.3-5V para cambiar entre estas dos tensiones en algunos pines de alimentación.
* Entradas y salidas analógicas.
* Sensor Hall y de temperatura integrado.
* 2 convertidores Digital-Analógico (DAC) de 8 bits.
* 16 convertidores Analógico-Digital (ADC) de 12 bits.
* 16 canales PWM.
* 2 UART.
* 2 canales I2C.
* 4 canales SPI.
* 448Kb ROM.
* 520 KB SRAM.
* 8KB+8KB SRAM en RTC.
* 1kbit eFUSE.
* 512 bytes Memoria Flash (EEPROM).
* 10 sensores táctiles.
* 4 temporizadores internos de 64 bits.


.. note::
   **¡Un Cerebro con Superpoderes!** 🧠
   A diferencia de las placas más antiguas, el ESP32 viene con **Wi-Fi y Bluetooth** integrados de fábrica. ¡Eso significa que tu placa puede conectarse a internet, hablar con tu teléfono móvil o recibir órdenes desde el otro lado de la habitación!

Los Músculos: Los Pines de Conexión (GPIO)
===========================================

¿Ves esas filas de agujeros amarillos en los bordes? Se llaman pines **GPIO** (**General Purpose Input/Output**, *Entrada/Salida de Propósito General*). 

.. image:: /_static/capitulo1/Pinout-ESP32.png
   :alt: Detalle de la placa
   :align: center
   :scale: 100%

Son los "músculos" y los "sentidos" de nuestra placa. Gracias a ellos podemos conectar cables para:

* **Dar órdenes (Salidas):** Encender luces LED, hacer sonar un zumbador o mover las ruedas de un robot.
* **Escuchar al mundo (Entradas):** Saber si un botón está pulsado o medir la luz de la habitación con un sensor.

.. warning::
   **¡Cuidado con la electricidad!** ⚡
   La placa funciona con un voltaje muy bajo y seguro para ti (3.3 Voltios o 5 Voltios). Pero recuerda: **¡nunca conectes cables a lo loco!** Si juntas la patita de energía (VCC) con la de tierra (GND) directamente sin pasar por un componente, causarás un **cortocircuito**. ¡Sigue siempre los esquemas como un auténtico profesional!

Algunos pines GPIO pueden tener un comportamiento no esperado durante el arranque del sistema o en el reinicio del mismo. Esto se debe a que durante el arranque de la placa ESP32 se deben realizar procesos internos que ponen en alto ciertos pines o incluso hacen que emitan señales, y esto puede provocar esos efectos no deseados.

El **pin GPIO1** del microcontrolador es el pin Tx del puerto UART de depuración y cuando la placa arranca, se reinicia o cuando nosotros hacemos uso del puerto serie, este pin emite datos. Por este motivo **es un pin que no conviene usar como entrada o salida**.

El **GPIO3** tiene un problema similar al GPIO1 ya que se trata del pin Rx del micocontrolador.

Los pines **GPIO34**, **GPIO35**, **GPIO36** y **GPIO39** solamente pueden utilizarse como entradas porque no disponen de resistencia pull-up.

Entradas Analógicas
=====================
Las señales analógicas son las que pueden tomar diferentes valores de tensión en un determinado periodo de tiempo, siendo su forma mas característica la senoidal. Cuando hablamos de entradas analógicas estamos hablando de pines del microcontrolador que pueden leer esas señales. En el caso de ESP32 todo son pines GPIO y por lo tanto se requiere de un conversor analógico a digital que sea capaz de transformar esas señales analógicas en digitales. El chip ESP32 que monta la placa ESP32 STEAMakers dispone de 2 convertidores Digital-Analógico (DAC) de 8 bits y 16 convertidores Analógico-Digital (ADC) de 12 bits. Estos conversores se asocian a los pines IO1 hasta IO20.

La resolución de los conversores ADC es de 12 bits (2^12 = 4096) por lo que la transformación de los valores digitales va a ser de mucha precisión. Pero cuidado con el uso de estas entradas, porque en realidad su comportamiento es que están leyendo valores digitales y no valores analógicos por lo que cambios de valores analógicos muy pequeños pueden no ser detectados.

Los canales ADC se dividen en dos puertos denominados ADC1 y ADC2. Las entradas analógicas del puerto ADC2 solamente las podemos usar como tales si el controlador WiFi no ha sido iniciado, ya que este puerto es el que utiliza el controlador del WiFi que integra la placa.

Entradas y Salidas Digitales
=============================
Una señal digital solamente puede tomar dos valores o estados lógicos, alto y bajo, High y Low, 0 y 1 siendo su representación característica una onda cuadrada. El estado bajo se asocia a cero voltios y el estado alto a 3.3V (5V en el caso de placa tipo UNO).

Las entradas permiten recibir señales con los valores digitales descritos, como por ejemplo leer el estado de un pulsador.

Debemos saber que ESP32 lleva unas resistencias de pull-up (1) o pull-down (0) que nos permiten establecer el estado que tiene la entrada cuando está en reposo. Estas resistencias están disponibles en todos los pines excepto el 34 y 39. Estas resistencias internas se pueden activar por código.

Las salidas digitales nos van a servir para realizar acciones sobre los elementos conectadas en ellas, como por ejemplo encender un LED o activar un relé.

En principio todos los pines que se pueden utilizar como salida en ESP32 pueden usarse con PWM excepto los pines que no disponen de resistencia de pull-up interna.

¿Cómo le damos energía?
=======================

Para que el cerebro despierte, necesita "comida". Tienes dos formas de darle energía:

* El conector **USB**: Sirve para conectarlo a tu Mac. No solo le da electricidad, ¡también es el túnel por el que le enviaremos nuestros códigos de programación!
* El conector de **Batería**: Para cuando tu proyecto esté terminado (por ejemplo, un coche robot) y quieras que funcione libremente por el suelo sin cables.

¡Tu turno de inspección!
=========================

.. note::
   Coge tu placa de STEAMakers con cuidado por los bordes. Busca el chip cuadrado del ESP32 y localiza el pequeño circuito integrado. ¿Eres capaz de encontrar dónde está escondida la antena de Wi-Fi? (Pista: suele ser una línea blanca o una zona con una pista de cobre en forma de zigzag).
