import matplotlib.pyplot as plt
import numpy as np

n = np.arange(200)
y = np.empty(200)

def problem5(x):
    
    for z in n:
        
        #converts z in n into integers
        r = int(z)
        
        #piecewise functions that does the statement inside the if condition
        #and stores it in y for plotting later
        if z == 0:
            y[r] = -1.5*x[r] + 2*x[r+1] - 0.5*x[r+2]
            
            
        elif z > 0 and z <= 198:
            y[r] = 0.5*x[r+1] - 0.5*x[r-1]
            
            
        elif z == 199:
            y[r] = 1.5*x[r] - 2*x[r-1] + 0.5*x[r-2]
            
            
            
    plt.plot(n,x, label='x(n)')   
    plt.plot(n,y, label='y(n)')
    plt.xlabel('x-axis')
    plt.ylabel('y-axis')
    plt.legend()
    plt.show()


