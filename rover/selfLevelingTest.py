from mpu6050 import mpu6050
import RPi.GPIO as GPIO
import time
import math
import dcmotors as motor
motor = motor.Motor(pwm_pin=10, stby_pin=7, in1_pin=11, in2_pin=9)

class SelfLeveling():
    def __init__(self):
        #mpu = self.mpu6050(0x68)
        GPIO.setwarnings(False)
        GPIO.setmode(GPIO.BCM)
        self.rightLegAngle = 0
        self.leftLegAngle = 90
        self.leveled = False
        GPIO.setup(12, GPIO.OUT)
        GPIO.setup(13, GPIO.OUT)
        self.p1 = GPIO.PWM(12, 50)
        self.p2 = GPIO.PWM(13, 50)
        self.p1.start(0)
        self.p2.start(0)


    def get_pwm(self, angle):
        return (angle/18.0) + 2.5
    
    def set_straight(self, standing:bool):
        while standing:
            self.p1.ChangeDutyCycle(self.get_pwm(80))
            self.p2.ChangeDutyCycle(self.get_pwm(80))
        #time.sleep(2)
        #self.p1.start(0) # Reduces jitter, must have a time.sleep 
        #self.p2.start(0)
        
    
    def level(self,pitch, tresh1, tresh2):
        if pitch <= tresh1 and pitch >= tresh2:
            self.p1.start(0) # Reduces jitter, must have a time.sleep 
            self.p2.start(0)
            self.leveled = True
        
        elif pitch > tresh1:
            self.rightLegAngle += 1
            self.p1.ChangeDutyCycle(self.get_pwm(self.rightLegAngle))
       
        elif pitch < tresh2:
            self.leftLegAngle += 1
            self.p2.ChangeDutyCycle(self.get_pwm(self.leftLegAngle))


#in main loop, if mpu data is too far from ideal, then restart the process
#l = SelfLeveling()
#l.set_straight()
# while True:
#     ax = mpu.get_accel_data().get("x")
#     ay = mpu.get_accel_data().get("y")
#     az = mpu.get_accel_data().get("z")
#     print(ax,ay,az)
    #pitch = math.atan2(-ax, az) ignore for now, working with az  #print(pitch)
#    if l.leveled == False:
#        l.level(az)
        
#    if az > 0 or az < -1.3:
#        l.leveled = False 
#GPIO.cleanup()

motor.motorForward()
time.sleep(2)
motor.motorStop()
time.sleep(1)
s = SelfLeveling()
s.set_straight(True)


