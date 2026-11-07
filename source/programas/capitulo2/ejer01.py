'''
---------------------------------------------------------------------
Programa: ejer01.py

Descripción: Encendido de un led con la placa ESP32 de STEAMakers

Observaciones:

    GPIO del led --> 26 (D2)
    No descargamos el programa en la placa de momento, lo guardamos en
    nuestro ordenador y lo ejecutamos con la placa conectada. El led
    deberá encenderse/apagarse según el intervalo establecido
---------------------------------------------------------------------
'''

from machine import Pin
from time import sleep_ms
 
GPIO_LED = 26	#D2

led = Pin(GPIO_LED, Pin.OUT, value=0)


while True:
    led.value(1)
    sleep_ms(500)
    led.value(0)
    sleep_ms(500)