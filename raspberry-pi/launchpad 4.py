from adafruit_motor import servo
import pwmio
import board
import digitalio
import time

led = digitalio.DigitalInOut(board.GP15)
led2 = digitalio.DigitalInOut(board.GP16)
led.direction = digitalio.Direction.OUTPUT
led2.direction = digitalio.Direction.OUTPUT
button = digitalio.DigitalInOut(board.GP0)
button.direction = digitalio.Direction.INPUT
button.pull = digitalio.Pull.DOWN
pwm_servo = pwmio.PWMOut(board.GP17, duty_cycle=2 ** 15, frequency=50)
servo1 = servo.Servo(pwm_servo, min_pulse=500, max_pulse=2500)
servo1.angle = 180

while True:
  print(button.value)

  if(button.value == True):
    for x in range(10, 0, -1):
      time.sleep(.25)
      print (x)
      time.sleep(.25)
      led.value = True
      time.sleep(.25)
      led.value = False
      time.sleep(.25)
    time.sleep(.25)
    print("liftoff")
    servo1.angle = 0
    while True:
      led2.value = True
