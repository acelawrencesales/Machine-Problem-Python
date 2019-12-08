import numpy as np

#This function takes an nx2 matrix as input and gives the coefficients of
#the polynomial that best approximates the data values, as output.
def problem3(p):
    
    x = p[:,0]
    y = p[:,1]
    
    m = len(x)
    n = len(y)
    
    e = []
    e2 = []
    e3 = []
    e4 = []
    e5 = []
    e6 = []
    e7 = []
    e8 = []
    e9 = []
    e10 = []
    z = []
    
    #These conditions determine the polynomials that can be drawn from the data
    #The np.linalg.norm() is used to determine the least-norm error vector
    if n >=2 and m >= 2:
        d = np.polyfit(x,y,1)
        q = np.polyval(d,x)
        e = y - q
        a = np.linalg.norm(e)
        z.append(a)
        
    if n >=3 and m >= 3:
        d2 = np.polyfit(x,y,2)
        q2 = np.polyval(d2,x)
        e2 = y - q2
        a2 = np.linalg.norm(e2)
        z.append(a2)
        
    if n >=4 and m >= 4:
        d3 = np.polyfit(x,y,3)
        q3 = np.polyval(d3,x)
        e3 = y - q3
        a3 = np.linalg.norm(e3)
        z.append(a3)
        
    if n >=5 and m >= 5:
        d4 = np.polyfit(x,y,4)
        q4 = np.polyval(d4,x)
        e4 = y - q4
        a4 = np.linalg.norm(e4)
        z.append(a4)
        
    if n >=6 and m >= 6:
        d5 = np.polyfit(x,y,5)
        q5 = np.polyval(d5,x)
        e5 = y - q5
        a5 = np.linalg.norm(e5)
        z.append(a5)
        
    if n >=7 and m >= 7:
        d6 = np.polyfit(x,y,6)
        q6 = np.polyval(d6,x)
        e6 = y - q6
        a6 = np.linalg.norm(e6)
        z.append(a6)
        
    if n >=8 and m >= 8:
        d7 = np.polyfit(x,y,7)
        q7 = np.polyval(d7,x)
        e7 = y - q7
        a7 = np.linalg.norm(e7)
        z.append(a7)
        
    if n >=9 and m >= 9:
        d8 = np.polyfit(x,y,8)
        q8 = np.polyval(d8,x)
        e8 = y - q8
        a8 = np.linalg.norm(e8)
        z.append(a8)
        
    if n >=10 and m >= 10:
        d9 = np.polyfit(x,y,9)
        q9 = np.polyval(d9,x)
        e9 = y - q9
        a9 = np.linalg.norm(e9)
        z.append(a9)
        
    if n >=11 and m >= 11:
        d10 = np.polyfit(x,y,10)
        q10 = np.polyval(d10,x)
        e10 = y - q10
        a10 = np.linalg.norm(e10)
        z.append(a10)
        
    k = min(z)
    #One of these statements would output the coefficients of the polynomial
    #with the least value.
    if k == a:
        print('The coefficients of the best polynomial: \n')
        print(d)
    elif k == a2:
        print('The coefficients of the best polynomial: \n')
        print(d2)
    elif k == a3:
        print('The coefficients of the best polynomial: \n')
        print(d3)
    elif k == a4:
        print('The coefficients of the best polynomial: \n')
        print(d4)
    elif k == a5:
        print('The coefficients of the best polynomial: \n')
        print(d5)
    elif k == a6:
        print('The coefficients of the best polynomial: \n')
        print(d6)
    elif k == a7:
        print('The coefficients of the best polynomial: \n')
        print(d7)
    elif k == a8:
        print('The coefficients of the best polynomial: \n')
        print(d8)
    elif k == a9:
        print('The coefficients of the best polynomial: \n')
        print(d9)
    elif k == a10:
        print('The coefficients of the best polynomial: \n')
        print(d10)
    else:
        return