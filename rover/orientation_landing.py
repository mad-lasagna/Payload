from mpu6050 import mpu6050

mpu = mpu6050(0x68)

gyro_data = mpu.get_gyro_data()

zAxis = gyro_data.get('z')

def dcMotorsDirection(zAxis):
    if zAxis > 0:
        motor1.motorForward()
        motor2.motorForward()
    else:
        motor1.motorBackward()
        motor2.motorBackward()