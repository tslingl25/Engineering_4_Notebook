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