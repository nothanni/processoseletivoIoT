import time
import random
from machine import Pin

led_vermelho = Pin(23, Pin.OUT)
led_verde = Pin(22, Pin.OUT)

temperatura = 20.0

print("Monitor de Temperatura")

while True:
    if temperatura >= 25:
        temperatura += random.uniform(-3, 1)
    else:
        temperatura += random.uniform(-1, 3)
    
    temperatura = max(15, min(35, temperatura))
    
    print(f"Temperatura atual: {temperatura:.2f}°C")
    
    if temperatura >= 25:
        led_vermelho.on()
        led_verde.off()
        print("LED VERMELHO ligado (temperatura alta)")
    else:
        led_vermelho.off()
        led_verde.on()
        print("LED VERDE ligado (temperatura normal)")
    
    time.sleep(1)