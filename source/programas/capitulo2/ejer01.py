from machine import Pin
from time import sleep_ms
 
GPIO_LED = 26	#D2

led = Pin(GPIO_LED, Pin.OUT, value=0)


while True:
    led.value(1)
    sleep_ms(500)
    led.value(0)
    sleep_ms(500)