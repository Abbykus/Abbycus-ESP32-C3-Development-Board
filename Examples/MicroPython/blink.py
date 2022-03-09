import machine
import time
led = machine.Pin(9, machine.Pin.OUT)  # GPIO 9 is the LED on QDEV-ESP32-C3
for i in range(30):
   led.off()
   time.sleep(0.5)
   led.on()
   time.sleep(0.5)
 
