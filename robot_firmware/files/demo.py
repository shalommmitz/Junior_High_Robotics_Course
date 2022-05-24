from machine import Pin as pin, PWM
import utime, rf, os, ubinascii
import display, time

OFF = 0; ON = 1 
LED_OFF = 1; LED_ON = 0 
FORWARD = 1; BACK = 0
pwmRight = pin(14,pin.OUT)
dirRight = pin(15,pin.OUT)
pwmLeft = pin(12,pin.OUT)
dirLeft = pin(0,pin.OUT)
LED = pin(2,pin.OUT)
LED.value(LED_OFF)


while True:
    # Step 1: get and blink robot ID
    ROBOT_ID = 2
    if 'robot_id' in os.listdir():
        f = open("robot_id")
        robot_id_str = f.read()
        robot_id_str = robot_id_str.replace(chr(10), "").strip()
        ROBOT_ID = int( robot_id_str )
        f.close()

    print("Robot id is", ROBOT_ID)
    utime.sleep(1)
    for i in range(ROBOT_ID):
        LED.value(LED_ON); utime.sleep(1)
        LED.value(LED_OFF); utime.sleep(1)

    # Step 2: Test motors
    print("Step 2: Test motors")
    dirRight.value(FORWARD); dirLeft.value(FORWARD)
    pwmRight.value(ON);  pwmLeft.value(ON);  utime.sleep(3)
    pwmRight.value(OFF); pwmLeft.value(OFF); utime.sleep(1)
    dirRight.value(BACK); dirLeft.value(BACK)
    pwmRight.value(ON);  pwmLeft.value(ON);  utime.sleep(3)
    pwmRight.value(OFF); pwmLeft.value(OFF); utime.sleep(1)
    LED.value(LED_OFF)

    # Step 3: Test display
    print("Step 3: Test display")
    d = display.Display()
    d.clear()
    d.hexImage("iAmTheRobot.hexImage")
    time.sleep(1)
    d.clear()
    d.hexImage("ofOfek.hexImage")
    time.sleep(1)
    d.clear()
    d.hexImage("painting.hexImage")
    time.sleep(1)
