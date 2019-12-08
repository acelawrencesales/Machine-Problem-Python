import numpy as np
import math

def problem2(x1,y1,x2,y2,x3,y3):
    
    x1s = x1**2 + y1**2
    x2s = x2**2 + y2**2
    x3s = x3**2 + y3**2
    
    #this is used to determine the values of Ax^2 + Ay^2 + Dx + Ey + F = 0
    #by arranging it in matrices based on input values
    A = np.array([(x1, y1, 1), (x2, y2, 1), (x3, y3, 1)])
    
    D = -np.array([(x1s, y1, 1), (x2s,
                  y2, 1), (x3s, y3, 1)])
    E = np.array([(x1s, x1, 1), (x2s,
                  x2, 1), (x3s, x3, 1)])
    F = -np.array([(x1s, x1, y1), (x2s,
                  x2, y2), (x3s, x3, y3)])
    
    #np.linalg.det() is used to determine the determinant
    detA = round(np.linalg.det(A))
    detD = round(np.linalg.det(D))
    detE = round(np.linalg.det(E))
    detF = round(np.linalg.det(F))
    
    #this part simplifies the equation of the circle
    simplifyD = round((detD / detA), 4)
    simplifyE = round((detE / detA), 4)
    simplifyF = round((detF / detA), 4)
    
    #this part finds the center of the circle using the determinants of the matrices
    h = round(-(detD / (2*detA)), 4)
    k = round(-(detE / (2*detA)), 4)
    
    #this part determines the radius
    r = round(math.sqrt((h - x1)**2 + (k - y1)**2), 4)
    
    print('The center of the circle is (', h,',', k,')')
    print('The radius of the circle is r = ', r)
    print('vector [', simplifyD,',', simplifyE,',', simplifyF,']')