from machine import Pin
from time import sleep_ms
 
GPIO_LED = 26	#D2
GPIO_BOTON = 25 #D3
 
led = Pin(GPIO_LED, Pin.OUT, value=0)
boton = Pin(GPIO_BOTON, Pin.IN, Pin.PULL_UP)

while True:
    pulsado = boton.value()
    print(pulsado)
    
    if pulsado == 0:
        led.value(1)
    else:
        led.value(0)
    sleep_ms(50)    