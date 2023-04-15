import RPi.GPIO as GPIO
import time

GPIO.setwarnings(False)
# Set up the GPIO pins
class Stepper:
    def __init__(self) -> None:
        self.DIR = 27
        self.STEP = 22
        self.CW = 1
        self.CCW = 0
        self.delay = 0.001
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.DIR, GPIO.OUT)
        GPIO.setup(self.STEP, GPIO.OUT)



    def step_motor(self,direction, angle):
        # Convert angle to number of steps
        STEPS_PER_REV = 2048
        steps = int(angle / 360 * STEPS_PER_REV)

        # Set the direction of rotation
        if direction == 1:
            GPIO.output(self.DIR, self.CW)
        else:
            GPIO.output(self.DIR, self.CCW)

        # Step the motor
        for i in range(steps):
            GPIO.output(self.STEP, GPIO.HIGH)
            time.sleep(self.delay)
            GPIO.output(self.STEP, GPIO.LOW)
            time.sleep(self.delay)

# Example usage
#s = Stepper()

#s.step_motor(1, 60)
#time.sleep(3)
#s.step_motor(0,60)
#time.sleep(1)
#s.step_motor(1,360)
# # Clean up the GPIO pins
#GPIO.cleanup()
