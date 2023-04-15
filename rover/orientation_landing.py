from mpu6050 import mpu6050
import math
import time
mpu = mpu6050(0x68)


def checkTilt(aX, aY, aZ):

    pitch = math.atan2(-1 * aX, aZ) * 180 / math.pi  # rotation on Y axis
    roll = math.atan2(-1 * (aY), aZ) * 180 / math.pi  # rotation on X axis

    if abs(roll) > 90 or abs(pitch) > 90:
        print("Rover is upside down")
        return 0
            
#    elif (roll > 0 and pitch < 0) or (roll < 0 and pitch > 0):
#        print("Rover is upside down")
#        return 0
    else:
        print("Rover is not upside down")
        return 1
while True:
    accelerometer_data = mpu.get_accel_data(g=True)
    ax = round(accelerometer_data.get('x'), 1)
    ay = round(accelerometer_data.get('y'), 1)
    az = round(accelerometer_data.get('z'), 1)
    print(ax,ay,az)
    checkTilt(ax,ay,az)
    time.sleep(0.5)
    
