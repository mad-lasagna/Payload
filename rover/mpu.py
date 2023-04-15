from mpu6050 import mpu6050
from gpiozero import Buzzer
import math
import time
import record
from datetime import datetime


class MPU:
    def __init__(self) -> None:
        self.mpu = mpu6050(0x68)
        self.buzzer = Buzzer(25)  # enter GPIO pin
        self.mpu.set_accel_range(self.mpu.ACCEL_RANGE_16G)
        self.landCheck = False
        self.landCount = 0
        self.LANDED = False

    def checkTilt(self,aX, aY, aZ):

        pitch = math.atan2(-1 * aX, aZ) * 180 / math.pi  # rotation on Y axis
        roll = math.atan2(-1 * (aY), aZ) * 180 / math.pi  # rotation on X axis

        if abs(roll) > 90 or abs(pitch) > 90:
            print("Rover is upside down")
            return 0
            
        elif (roll > 0 and pitch < 0) or (roll < 0 and pitch > 0):
            print("Rover is upside down")
            return 0
        else:
            print("Rover is not upside down")
            return 1
        
    def landingDetection(self):
        while True:

            temperature = 0

            accelerometer_data = self.mpu.get_accel_data(g=True)
            gyro_data = self.mpu.get_gyro_data()
            
            print(accelerometer_data.get('x'), 1)
            if round(accelerometer_data.get('x'), 1) > 7 or round(accelerometer_data.get('x'), 1) < -7:
                landCheck= True
                print("Launched")

            prevX = round(accelerometer_data.get('x'), 1)
            prevY = round(accelerometer_data.get('y'), 1)
            prevZ = round(accelerometer_data.get('z'), 1)

            time.sleep(0.33)

            accelerometer_data = self.mpu.get_accel_data(g=True)
            ax = round(accelerometer_data.get('x'), 1)
            ay = round(accelerometer_data.get('y'), 1)
            az = round(accelerometer_data.get('z'), 1)

            print('X: ' + str(prevX) + ' Y: ' + str(prevY) + ' Z: ' + str(prevZ))
            print('X: ' + str(ax) + ' Y: ' + str(ay) + ' Z: ' + str(az))

            if landCheck:
                # LANDED CODE
                if (ax == prevX) and (ay == prevY) and (az == prevZ):
                    print('Landed!!!')
                    self.landCount += 1
                    if self.landCount >= 15:
                        self.LANDED = True
                    print(self.checkTilt(ax, ay, az))

                # NOT LANDED, STILL MOVING
                else:
                    print('Schmooving!')
                    self.LANDED = False
                    self.landCount = 0

            temp = []
            date_str = str(datetime.now())

            current_time = datetime.strptime(date_str, '%Y-%m-%d %H:%M:%S.%f')
            t = time.localtime()
            # current_time = time.strftime("%M:%S", t)

            temperature = self.mpu.get_temp()

            temp.append(current_time)
            temp.append(ax)
            temp.append(ay)
            temp.append(az)
            temp.append(self.LANDED)
            temp.append(temperature)

            pitch = math.atan2(-1 * ax, az) * 180 / math.pi  # rotation on Y axis
            temp.append(pitch)
            roll = math.atan2(-1 * (ay), az) * 180 / math.pi  # rotation on X axis
            temp.append(roll)

            print(self.checkTilt(ax, ay, az))

            if self.LANDED:

                print("Landed")

                # Record one more time for statistics
                record.record(temp)

                break

                while True:
                    self.buzzer.on()

                    exit()
            else:
                record.record(temp)

            self.buzzer.on()
            time.sleep(0.5)
            self.buzzer.off()

    def printVals(self):
        accelerometer_data = self.mpu.get_accel_data(g=True)
        ax = round(accelerometer_data.get('x'), 1)
        ay = round(accelerometer_data.get('y'), 1)
        az = round(accelerometer_data.get('z'), 1)
        print(ax, ay, az)
