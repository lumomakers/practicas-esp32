from machine import Pin, ADC
from time import sleep_ms
 
ldr = ADC(Pin(34))
GPIO_LED = 26 

led = Pin(GPIO_LED, Pin.OUT, value=0)

while True:
    # read_u16 devuelve el valor crudo entre 0 y 65535
    nivel_luz = ldr.read_u16()
    
    # Calculamos el porcentake para que sea más fácil de interpretar
    porcentaje = (nivel_luz / 65535) * 100
    

    print(f"Valor ADC: {nivel_luz} | Luz: {porcentaje:.1f}%")
    
    if (nivel_luz < 40000):
        led.value(1)
    else:
        led.value(0)
     
    # Pequeña pausa para no saturar
    sleep_ms(500)
    
  