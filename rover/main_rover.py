import time
import RPi.GPIO as GPIO
import mpu
import dcmotors as motor
import selfLevelingTest as leveling
import cam as cam
import stepper_motor as stepper
import sub_process

motor = motor.Motor(pwm_pin=10, stby_pin=7, in1_pin=11, in2_pin=9)
camera = cam.Camera()
servoLeveling = leveling.SelfLeveling()
stepper = stepper.Stepper()
mpu = mpu.MPU()
sub = sub_process.Subprocess()

greyscale = False
flip = False
filters = False

# A1—Turn camera 60o to the right
# B2—Turn camera 60o to the left
# C3—Take picture
# D4—Change camera mode from color to grayscale E5—Change camera mode back from grayscale to color F6—Rotate image 180o (upside down).
# G7—Special effects filter (Apply any filter or image distortion you want and state what filter or distortion was used).
# H8—Remove all filters.
commands = ["A1", "B2", "C3", "D4", "E5", "F6", "G7", "H8"]
    

def Commands(command):
    if command == commands[0]:
        stepper.step_motor(1,60)
        time.sleep(2)
    if command == commands[1]:
        stepper.step_motor(0,60)
        time.sleep(2)
    if command == commands[2]:
        camera.take_picture(greyscale,flip,filters)
    if command == commands[3]:
        greyscale = True
    if command == commands[4]:
        greyscale = False
    if command == commands[5]:
        flip != flip
    if command == commands[6]:
        filters = True
    if command == commands[7]:
        filters = False


def callCommands(sentCommands):
    for i in range(len(sentCommands)):
        Commands(sentCommands[i])
        time.sleep(2)
    exit()

def startOnceUpright():
    sub.subprocess()
    EMPTY = True
    while EMPTY:
        f = open("output.txt", 'r')
        lines = f.readlines()
        found = False
        count = 0
        for line in lines:
            if found:
                x = (line[line.find(".X/'") + 4:line.find("_")])
                sent_commands = x.split()
                print(sent_commands)
                break
            time.sleep(1)
            count += 1
            if count >= 15:
                sent_commands = ["C3", "A1", "D4", "C3", "E5", "A1", "G7", "C3", "H8", "A1", "F6", "C3"]
                break
            if "KQ4CTL-6" in line:
                found = True
                EMPTY = False
    comandFile = open("comandFile.txt", "w")
    for item in sent_commands:
        comandFile.write(item+"\n")
    comandFile.close()
    callCommands(sent_commands)

def startOnceLanded(forward: bool):
    # tresh1 = 0
    # tresh2 = 0
    # az = mpu.mpu.get_accel_data().get("z")
    if forward:
        motor.motorForward()
    else:
        motor.motorBackward()
    time.sleep(2)
    motor.motorStop()
    time.sleep(1)
    # servoLeveling.set_straight()
    #add any other code to set straight
    # servoLeveling.level(az,tresh1,tresh2)
    # while servoLeveling.leveled == False:
    #     servoLeveling.level(az,tresh1,tresh2)
    time.sleep(1)
    GPIO.cleanup()
    #startOnceUpright()

def startFromLaunch():
    mpu.landingDetection()
    if mpu.LANDED == True:
        time.sleep(5)
        startOnceLanded(mpu.checkTilt)

    
def start():
    startFromLaunch()

def skipStart():
    startOnceLanded(1)

#start()
skipStart()
