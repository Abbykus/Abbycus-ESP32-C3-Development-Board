import machine
import time
pin = machine.Pin(9, machine.Pin.OUT)  # GPIO 9 is the LED on QDEV-ESP32-C3
for i in range(30):
   pin.off()
   time.sleep(0.5)
   pin.on()
   time.sleep(0.5)
 
