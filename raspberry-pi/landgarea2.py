import board
import busio
from adafruit_display_text import label
import adafruit_displayio_ssd1306
import displayio
from adafruit_display_shapes.triangle import Triangle
from adafruit_display_shapes.line import Line
from adafruit_display_shapes.circle import Circle
displayio.release_displays()

sda_pin = board.GP12   
scl_pin = board.GP13 
i2c = busio.I2C(scl_pin, sda_pin) 
display_bus = displayio.I2CDisplay(i2c, device_address=0x3d, reset=board.GP11)
display = adafruit_displayio_ssd1306.SSD1306(display_bus, width=128, height=64)

def triangle_area(x1y1,x2y2,x3y3):   
    try:    
        x1y1 = x1y1.split(",")
        x2y2 = x2y2.split(",")
        x3y3 = x3y3.split(",")
        x1 = float(x1y1[0])
        y1 = float(x1y1[1])
        x2 = float(x2y2[0])   
        y2 = float(x2y2[1])   
        x3 = float(x3y3[0])
        y3 = float(x3y3[1])
        area = (1/2)*abs(x1*(y2-y3) + x2*(y3-y1) + x3*(y1-y2))   
        splash = displayio.Group() 
        hline = Line(64,0,64,64, color=0xFFFF00)
        splash.append(hline)      
        vline = Line(0,32,128,32, color=0xFFFF00)
        splash.append(vline) 
        circle = Circle(64, 32, 4, outline=0xFFFF00)
        splash.append(circle)
        triangle = Triangle(int(x1)+64, -int(y1)+32, int(x2)+64, -int(y2)+32, int(x3)+64, -int(y3)+32, outline=0xFFFF00)
        splash.append(triangle)
        display.show(splash)
        return area

    except:   
        print("Not a triangle dum dum!")
        area = 0
        return area
while True:

    print ("enter first coordinate")
    x1y1 = input()
    print ("enter second coordinate")
    x2y2 = input()
    print ("enter third coordinate")
    x3y3 = input()

    area = triangle_area(x1y1,x2y2,x3y3)  

    if area == 0:
        continue
    else:  
        area = print(f"{x1y1} + {x2y2} + {x3y3} = {area} square km.")
