import machine
import time
pin = machine.Pin(2, machine.Pin.OUT) # GPIO 2 is the ESP-12F LED
for i in range(30):
   pin.off()
   time.sleep(0.5)
   pin.on()
   time.sleep(0.5)
 
