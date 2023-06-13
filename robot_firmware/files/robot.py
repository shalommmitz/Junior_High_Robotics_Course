from machine import Pin as pin, PWM
import utime, rf, os, ubinascii

OFF = 0; ON = 1 
LED_OFF = 1; LED_ON = 0 
FORWARD = 1; BACK = 0
pwmRight = pin(14,pin.OUT)
dirRight = pin(15,pin.OUT)
pwmLeft = pin(12,pin.OUT)
dirLeft = pin(0,pin.OUT)
LED = pin(2,pin.OUT)
LED.value(LED_OFF)

def setRobotId(id):
    f = open("robot_id", 'w')
    f.write(str(id) + chr(10))
    f.close()

def executePacket(msgDict):
    print ("Executing:")
    for k in msgDict.keys():
        print("   ", k, msgDict[k])
    if msgDict["rightMotorDirction"] == "FORWARD":
        dirRight.value(FORWARD)
    else:
        dirRight.value(BACK)
    if msgDict["leftMotorDirction"] == "FORWARD":
        dirLeft.value(FORWARD)
    else:
        dirLeft.value(BACK)
    pwmRight.value(ON);  pwmLeft.value(ON)
    print("Motors will be on for", msgDict["rightMotorDuration"]/100)
    utime.sleep(msgDict["rightMotorDuration"]/100)
    pwmRight.value(OFF); pwmLeft.value(OFF)


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

# Step 3: Enter rf-recption mode, if received valid command before time-out
print("Step 3: Enter rf-recption mode")
# Step 3.1: make led blink: 
#           50% duty cycle, 4 Hz. Led is 0.125 sec on and 0.125 sec off
pwm = PWM(LED, freq=4, duty=512) 
utime.sleep(1)
pwm.deinit(); LED.value(LED_ON)
# Step 3.2: Wait for 10 seconds for valid command
r = rf.RF()
end_time =  utime.time() + 10
packet = None
while (utime.time()<end_time) and not packet:
    packet = r.getPacket()
    print("Got packet of len", len(packet))
    if len(packet)==0: packet = False
# Step 3.3: Switch off the LED and deinitialize/stop the timer
LED.value(LED_OFF)
# Step 3.4: Valid packet received - wait for more packets until reset 
if packet:
    while True:
        if packet: 
            print( "Got RF packet:"+ str(ubinascii.hexlify(packet)) )
            msgDict = r.interpetMsg( packet)
            print( "packet fields:"+ str(msgDict) )
            if "Error" in msgDict.keys():
                print("Ignoring rf packet because it is not well formed")
            elif str(msgDict["remoteId"]) != str(ROBOT_ID):
                print("Ignoring rf packet: wrong robot ID. Expected:"+ str(ROBOT_ID) +" Got from rf:"+ str(msgDict["remoteId"]) )
            else:
                executePacket(msgDict)
        packet = r.getPacket()

# Step 3.5: No valid packet received - will exit
print("Done")

