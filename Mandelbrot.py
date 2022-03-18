import matplotlib.pyplot as plt
import numpy as np
np.warnings.filterwarnings("ignore")

#-=Functions=-

#Prereq for graphing complex plain
def complex_matrix(xmin, xmax, ymin, ymax, pixel_density):
    re = np.linspace(xmin, xmax, int((xmax - xmin) * pixel_density))
    im = np.linspace(ymin, ymax, int((ymax - ymin) * pixel_density))
    return re[np.newaxis, :] + im[:, np.newaxis] * 1j

#Recursion to check for valid set
def isStable(c, numItr):
    z = 0
    for _ in range(numItr):
        z = z ** 2 + c
    return abs(z) <= 2



#Testing Mandelbrot set
"""
Recursive function to check
if n is bounded

def z(n, c):
    if n == 0:
        return 0
    else:
        return z(n - 1, c) ** 2 + c

#Testing function
for n in range(10):
    print(f"z({n}) = {z(n, c=0)}")
"""