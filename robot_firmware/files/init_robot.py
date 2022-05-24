from machine import Pin as pin, PWM
import utime,  os

OFF = 0; ON = 1 
LED_OFF = 1; LED_ON = 0 
FORWARD = 1; BACK = 0
pwmRight = pin(14,pin.OUT)
dirRight = pin(15,pin.OUT)
pwmLeft = pin(12,pin.OUT)
dirLeft = pin(0,pin.OUT)
LED = pin(2,pin.OUT)
LED.value(LED_OFF)

pwmRight.value(OFF); pwmLeft.value(OFF); utime.sleep(0.1)
	
print("Blinking LED")
for i in range(4):
    LED.value(LED_ON); utime.sleep(0.3)
    LED.value(LED_OFF); utime.sleep(0.5)    


