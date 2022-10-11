
import adafruit_mpu6050
import busio
import board
import time
import digitalio

led = digitalio.DigitalInOut(board.GP0)
led.direction = digitalio.Direction.OUTPUT
sda_pin = board.GP14
scl_pin = board.GP15
i2c = busio.I2C(scl_pin, sda_pin)
mpu = adafruit_mpu6050.MPU6050(i2c)
mpu.acceleration

while True:
    time.sleep(.2)
    print(mpu.acceleration)
    if(mpu.acceleration[0] > 8) or (mpu.acceleration[2] < 3):
     led.value = True
    else:
        led.value = False