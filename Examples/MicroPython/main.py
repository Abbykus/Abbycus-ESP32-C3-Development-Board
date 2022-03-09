import machine
import time
led = machine.Pin(9, machine.Pin.OUT) # LED on the QDEV-ESP32-C3 is GPIO 9
for i in range(30):
   led.off()
   time.sleep(0.5)
   led.on()
   time.sleep(0.5)
 
