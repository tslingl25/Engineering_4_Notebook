from adafruit_display_text import label 
import adafruit_displayio_ssd1306
import adafruit_mpu6050
import busio
import board
import time
import digitalio
import terminalio
import displayio


sda_pin = board.GP14
scl_pin = board.GP15
i2c = busio.I2C(scl_pin, sda_pin)
displayio.release_displays()
display_bus = displayio.I2CDisplay(i2c, device_address=0x3d, reset=board.GP21)
led = digitalio.DigitalInOut(board.GP0)
led.direction = digitalio.Direction.OUTPUT
reset=board.GP21
display = adafruit_displayio_ssd1306.SSD1306(display_bus, width=128, height=64)
mpu = adafruit_mpu6050.MPU6050(i2c, address=0x68)
splash = displayio.Group()
title = "ANGULAR VELOCITY"
text_area = label.Label(terminalio.FONT, text=title, color=0xFFFF00, x=5, y=5)
splash.append(text_area)    
display.show(splash)


while True:
    splash = displayio.Group()
    title = "ANGULAR VELOCITY"
    text_area = label.Label(terminalio.FONT, text=title, color=0xFFFF00, x=5, y=5)
    splash.append(text_area)    
    
    title = str(mpu.gyro[0])
    title = str(mpu.gyro[1])
    title = str(mpu.gyro[2])
    text_area = label.Label(terminalio.FONT, text=title, color=0xFFFF00, x=5, y=20)
    splash.append(text_area)   

    time.sleep(.2)
    print(mpu.acceleration)
    if(mpu.acceleration[0] > 8) or (mpu.acceleration[2] < 3):
     led.value = True
    else:
        led.value = False

    display.show(splash)



