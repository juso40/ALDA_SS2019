import numpy as np
from math import sqrt

def kochSnowflake(level, lenght):
    if level == 0:
        pass
    else:
        kochSnowflake(level - 1, lenght/3)


b = np.array([[0,0], [1, 0], [1/2, sqrt(3)/2]])
b = np.append(b, [[1,1]], axis = 0)
print(b)
print(b[2])