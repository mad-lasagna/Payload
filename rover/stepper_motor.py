import RPi.GPIO as GPIO
import time

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
# step_motor(1, 60, 0.001)
# time.sleep(3)
# step_motor(0,60, 0.001)
# time.sleep(1)
# step_motor(1,360,0.001)
# # Clean up the GPIO pins
# GPIO.cleanup()
