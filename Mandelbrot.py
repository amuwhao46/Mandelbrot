import matplotlib.pyplot as plt
import numpy as np

"""
Recursive function to check
if n is bounded
"""
def z(n, c):
    if n == 0:
        return 0
    else:
        return z(n - 1, c) ** 2 + c

#Testing function
for n in range(10):
    print(f"z({n}) = {z(n, c=-1)}")