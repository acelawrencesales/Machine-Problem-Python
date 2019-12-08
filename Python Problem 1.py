import matplotlib.pyplot as plt 
import numpy as np

n = np.arange(100)
y = np.empty(100)
w = 0

for x in n:
    
    #converts x to integer
    x = int(x)
    
    #inputs the value of x if it is less than or equal to 9
    #and executes the statement then storing it to y afterwards
    if x <= 9:
        y[x] = x**2 - 7
        
    #inputs the value of x if it is greater than or equal to 10
    elif x >= 10:
        w = x
        #this while loop repeats the condition as long as w remains
        #greater than or equal to 10 following the piecewise condition
        #n >= 10. It then stores it to y afterwards
        while w >= 10:
            w = w - 10
            y[x] = w**2 - 7
    
    plt.stem(n, y, use_line_collection=True)
    plt.xlabel('n')
    plt.ylabel('f(n)')
    plt.title('Graph of f(n)')
    plt.show()
        