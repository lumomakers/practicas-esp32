from machine import Pin, ADC
from time import sleep_ms
 
ldr = ADC(Pin(34))
 

while True:
    # read_u16 devuelve el valor crudo entre 0 y 65535
    nivel_luz = ldr.read_u16()
    
    # Calculamos el porcentake para que sea más fácil de interpretar
    porcentaje = (nivel_luz / 65535) * 100
    

    print(f"Valor ADC: {nivel_luz} | Luz: {porcentaje:.1f}%")
    
    # Pequeña pausa para no saturar
    sleep_ms(500)
    
  