# Engineering_4_Notebook

&nbsp;

## Table of Contents
* [Raspberry_Pi_Assignment_Template](#raspberry_pi_assignment_template)
* [Onshape_Assignment_Template](#onshape_assignment_template)

&nbsp;

## Countdown

### Description 
Countdown on serial moniter from ten, then print "LIFTOFF"

### Evidence 
I have this as my evidence because there was no wireing or external function

import board 
import digitalio
import time


for x in range(10, 0, -1): #This shows that it will count down between 10 and -1
  time.sleep(.5)
  print (x)
  time.sleep(.5)
time.sleep(.5)
print("liftoff")


### Wiring
None
### Code
https://github.com/tslingl25/Engineering_4_Notebook/blob/main/raspberry-pi/code.py

### Reflection
This assignment was good for learning for me as I feel like it was really the first time ive coded. It is good to ask your neighbors for help, Ezhar was very helpful. Make sure your computer has all the needed librarys in the lib folder.

&nbsp;

## Launch Pad Part 2 (Lights)

### Description
Countdown from 10 seconds to 0 (liftoff). Print that countdown to the serial monitor.
Blink a red light each second of the countdown, and turn on a green LED to signify liftoff.

### Evidence 
![gif1](https://user-images.githubusercontent.com/71349802/194382350-03dc24a8-34e1-4804-8bcf-6beab65a4ade.gif)

### Wiring
![snippp0pppp](https://user-images.githubusercontent.com/71349802/194383034-36ef569f-26d4-4c10-ab9f-afbefe5a2db1.PNG)
### Code
![snippy](https://user-images.githubusercontent.com/71349802/194383375-ca548d2d-fda8-4574-954c-8b6e31e86aac.PNG)

### Reflection
This assignment included lots of laerning for me, there were no huge hang ups but it is definitly smart to copy your lines from old code as even the smallest thing can mess it up. Make sure you have your LED prongs oriented right. Make sure to use the right amount of power or use a resitor as you can fry alot of LEDs.

&nbsp;

## Launch Pad Part 3 (Button)

### Description
Countdown from 10 seconds to 0 (liftoff). Print that countdown to the serial monitor.Blink a red light each second of the countdown, and turn on a green LED to signify liftoff.Include a physical button that starts the countdown. 


### Evidence 
![giffyyssss](https://user-images.githubusercontent.com/71349802/194621135-c7985bb5-7883-425c-acad-edab784ceebc.gif)


### Wiring
![snippers1](https://user-images.githubusercontent.com/71349802/194621399-b6b97d0d-d0b1-41d8-aa76-12572d69e2be.PNG)


### Code
import board
import digitalio
import time

led = digitalio.DigitalInOut(board.GP15)
led2 = digitalio.DigitalInOut(board.GP16) #These are defineing which LED is which
led.direction = digitalio.Direction.OUTPUT
led2.direction = digitalio.Direction.OUTPUT
button = digitalio.DigitalInOut(board.GP0)
button.direction = digitalio.Direction.INPUT
button.pull = digitalio.Pull.DOWN

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
    while True: #This is to turn on the green LED
      led2.value = True

### Reflection
This assignment was pretty straight foward. It may be helpful to know that the button has four legs but you only need 2. Make sure that you dont mix up the pin number with the numbering on the side of the pico.


&nbsp;

## Launch Pad Part 4 (Servo)

### Description 
Countdown from 10 seconds to 0 (liftoff). Print that countdown to the serial monitor.Blink a red light each second of the countdown, and turn on a green LED to signify liftoff.Include a physical button that starts the countdown. Actuate a 180 degree servo on liftoff to simulate the launch tower disconnecting.

### Evidence 
![Gif](https://github.com/tslingl25/Engineering_4_Notebook/blob/main/images/blahhhh.gif)

### Wiring
![Wiring](https://user-images.githubusercontent.com/71349802/195159523-34621bbb-031e-4adc-aa78-fff005f2c74c.PNG)

### Code
https://github.com/tslingl25/Engineering_4_Notebook/commit/125b7fe05469b8bc9d31bba48ebbf2503a5d9ebc

### Reflection
The assignment itself was not hard but github was being VERY difficult. It wouldnt let be put my gif in, then it would let me put my code in. If you find yourself with github being annoying, just upload stuff too it like 100 times then it will eventually work.


&nbsp;

## Crash Avoidance Part 1 (Accelerometer)

### Description 
The module must have an accelerometer that continuously reports x, y, and z acceleration values on the serial monitor.

### Evidence 
![image](https://user-images.githubusercontent.com/71349802/195905884-8ce980cc-6d77-4220-9910-e220035758f9.png)
### Wiring
[Wiring](https://github.com/tslingl25/Engineering_4_Notebook/blob/main/images/WIN_20221011_14_01_31_Pro.jpg)
### Code
[https://github.com/tslingl25/Engineering_4_Notebook/blob/main/raspberry-pi/code.py
](https://github.com/tslingl25/Engineering_4_Notebook/blob/main/raspberry-pi/crashaviodence.py)
### Reflection
Assignment was straight forward but make sure you READ DIRECTIONS. It is easy to miss small but important things. It is important to copy chunks of code as a wrong capitalization or somthing small can mess it up.

&nbsp;

## Crash Avoidance Part 2 (Light + Powerboost)

### Description
The module must have an accelerometer that continuously reports x, y, and z acceleration values.The module must have an LED that turns on if the helicopter is tilted to 90 degrees. The module must be powered by a mobile power source. 


### Evidence
![image](https://user-images.githubusercontent.com/71349802/195912943-317976a8-38fa-422f-b9fb-50b84737352a.png)
### Wiring
[Wiring](https://github.com/tslingl25/Engineering_4_Notebook/blob/main/images/WIN_20221011_14_01_31_Pro.jpg)
### Code
https://github.com/tslingl25/Engineering_4_Notebook/blob/main/raspberry-pi/code.py

### Reflection
Make sure you run the code on the pico in code.py, and make sure the battery is charged. Also, code.py is special, you can not just make a document called code.py and expect it to work the same. I tried that and it did not work the same.

&nbsp;


## Crash Avoidance Part 3 (OLED)

### Description
The module must have an accelerometer that continuously reports x, y, and z acceleration values.The module must have an LED that turns on if the helicopter is tilted to 90 degrees. The module must be powered by a mobile power source. The module must have an onboard screen that prints x, y, and z angular velocity values (rad/s) rounded to 3 decimal places.

### Evidence
![image](https://user-images.githubusercontent.com/71349802/196249026-39dd6bff-6c5e-4511-86f3-0b8013831317.png)
### Wiring
![Wiring](https://user-images.githubusercontent.com/71349802/196249434-076a3ce6-47dd-4141-bec4-f646251b8645.png)

### Code
https://github.com/tslingl25/Engineering_4_Notebook/blob/main/raspberry-pi/code.py

### Reflection
Read directionas and make sure you use the right address for each device. Remember that the one you unplug is the one that wont run on the moniter. It is easy to mix up.


&nbsp;


## Landing Area Part 1 (Functions)

### Description
The code must ask for the user to input a set of three coordinates in (x,y) format. The triangle area must be determined using a function. If the user inputs coordinates incorrectly (letters or improper format) the code should return to the input stage, it should not throw an error or exit the script. The triangle area must be printed to the screen in this format: “The area of the triangle with vertices (x,y), (x,y), (x,y) is {area} square km. The code must return to the input stage after printing the area, and wait for user input.

### Evidence
![da ting](https://user-images.githubusercontent.com/71349802/197024371-7580fed4-8911-4aa2-9ded-2d23a83aad13.gif)

### Wiring
NONE

### Code
https://github.com/tslingl25/Engineering_4_Notebook/blob/main/raspberry-pi/code.py

### Reflection
This assignment started off stuck in the mud. Once I started reading diections it got eaisier. Looking at mr.millers more help code section heled alot as it provided a format.


&nbsp;

## Landing Area Part 2 (Plotting)

### Description
The code must ask for the user to input a set of three coordinates in (x,y) format. The triangle area must be determined using a function. If the user inputs coordinates incorrectly (letters or improper format) the code should return to the input stage, it should not throw an error or exit the script. The triangle area must be printed to the screen in this format: “The area of the triangle with vertices (x,y), (x,y), (x,y) is {area} square km. The code must return to the input stage after printing the area, and wait for user input. An onboard OLED screen must plot each triangle on a graph relative to the base location.

### Evidence
![image](https://user-images.githubusercontent.com/71349802/197593871-f19b71e9-a6f1-47bd-9a0a-018374835eeb.png)



### Wiring
![WIN_20221024_13_46_20_Pro](https://user-images.githubusercontent.com/71349802/197591932-df64e202-0e63-4a3d-9fac-645f0fa936eb.jpg)

### Code
https://github.com/tslingl25/Engineering_4_Notebook/blob/main/raspberry-pi/landgarea2.py

### Reflection
It is helpful to remember that when doing I2c stuff with only one I2C device, you dont need to use multiple addresses. Make sure you dont import more stuff than you need, as that can lead to a syntax error. Look over code for un-needed bits because that can mess up the final prduct. It is also important too make sure you have the pins right becasue they are numbered different than they actually are.

&nbsp;


## Onshape_Assignment_Template

### Assignment Description

Write your assignment description here. What is the purpose of this assignment? It should be at least a few sentences.

### Part Link 

[Create a link to your Onshape document](https://cvilleschools.onshape.com/documents/003e413cee57f7ccccaa15c2/w/ea71050bb283bf3bf088c96c/e/c85ae532263d3b551e1795d0?renderMode=0&uiState=62d9b9d7883c4f335ec42021). Don't forget to turn on link sharing in your Onshape document so that others can see it. 

### Part Image

Take a nice screenshot of your Onshape document. 

### Reflection

What went wrong / was challenging, how'd you figure it out, and what did you learn from that experience? Your goal for the reflection is to pass on knowledge that will make this assignment better or easier for the next person. Think about your audience for this one, which may be "future you" (when you realize you need some of this code in three months), me, or your college admission committee!

&nbsp;

## Media Test

Your readme will have various images and gifs on it. Upload a test image and test gif to make sure you've got the process figured out. Pick whatever image and gif you want!

### Test Link
[earth](https://www.google.com/maps)
### Test Image
![Baseball](images/usa-mlb-baseball.jpg)
### Test GIF
 ![Weird orange gif thing](images/weird%20orange%20thing.gif)


