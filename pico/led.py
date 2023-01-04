from machine import Pin
import time
delay=0.4
led = Pin(3, Pin.OUT)
speaker=Pin(2, Pin.OUT)
while True:
    speaker.value(0)
    led.value(1)
    time.sleep(delay)
    led.value(0)
    time.sleep(delay)
    speaker.value(0)
       