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

#forward = 1
#if forward:
#    motor.motorForward()
#else:
#    motor.motorBackward()
#time.sleep(5)
#motor.motorStop()
#tresh1 = 0
#tresh2 = 0
#az = mpu.mpu.get_accel_data().get("z")


#servoLeveling.set_straight()
#add any other code to set straight
#while servoLeveling.leveled == False:
#    servoLeveling.level(az,tresh1,tresh2)
time.sleep(1)

commands = ["A1", "B2", "C3", "D4", "E5", "F6", "G7", "H8"]
    

greyscale = False
flip = False
filters = False
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
    for i in sentCommands:
        Commands(sentCommands[i])
        time.sleep(2)

callCommands(commands)
