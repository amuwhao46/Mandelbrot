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

#-=Graphing=-

#Displays values only in the mandelbrot set
def getMembers(c, numItr):
    mask = isStable(c, numItr)
    return c[mask]

#plots image of Mandelbrot Set
c = complex_matrix(-2, 0.5, -1.5, 1.5, pixel_density=1024)
plt.imshow(isStable(c, numItr = 20), cmap = 'binary')
plt.gca().set_aspect("equal")
plt.axis("off")
plt.tight_layout()
plt.show()


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