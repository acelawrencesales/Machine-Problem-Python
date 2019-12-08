import matplotlib.pyplot as plt 
import math

def problem4(h,v,a,xa,ya):
    
    if ya >= 0:
        print('Error: acceleration in y must be less than 0')
        return
    
    #this is where the program will store the values for plotting later
    xval = []
    yval = []
    
    t = 0
    x = 0
    y = 0

    #Finding the x and y components of the velocity
    vx = v * math.cos(math.radians(a))
    vy = v * math.sin(math.radians(a))

    while(True):
        
        t = t + 0.001
        
        #these are position formulas that determines the position
        #and will be stored in xval = [] and yval = []
        x = vx * t + (0.5) * xa * t**2
        y = vy * t + (0.5) * ya * t**2 + h
        
        #stores every x and y values to xval and yval respectively
        xval.append(x)
        yval.append(y)
        
        if y < .001:
            break
    
    plt.plot(xval,yval)
    plt.xlabel('x-axis')
    plt.ylabel('y-axis')
    plt.title('Projectile Motion')
    plt.grid()
    plt.show()
    