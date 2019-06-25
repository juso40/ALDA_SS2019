import matplotlib.pyplot as plt
import math
from math import sqrt

def kochSnowflake(level):
    coordinates = [
                    (0., 0.),
                    (1., 0.),
                    (1/2, sqrt(3)/2)
                  ]
    if level == 0:
        return coordinates
    else:
        XY = []
        for _ in range(level):
            for i in range(len(coordinates)):
                newX = (coordinates[i][0] / 3) + (2 * coordinates[(i+1) % len(coordinates)][0] / 3)
                newY = (coordinates[i][1] / 3) + (2 * coordinates[(i+1) % len(coordinates)][1] / 3)
                third2 = (newX, newY)

                newX = (2 * coordinates[i][0] / 3) + (coordinates[(i+1) % len(coordinates)][0] / 3)
                newY = (2 * coordinates[i][1] / 3) + (coordinates[(i+1) % len(coordinates)][1] / 3)
                third1 = (newX, newY)

                vec2DX = third2[0] - third1[0]
                vec2DY = third2[1] - third1[1] 
                
                rotatedX = math.cos(math.radians(-60)) * vec2DX - math.sin(math.radians(-60)) * vec2DY
                rotatedY = math.sin(math.radians(-60)) * vec2DX + math.cos(math.radians(-60)) * vec2DY

                midpoint = (rotatedX + third1[0], rotatedY + third1[1])
            
                XY.extend([coordinates[i],
                            third1,
                            midpoint,
                            third2])
            coordinates = XY
        return XY
            
         
XY = kochSnowflake(9)
#X = [i[0] for i in XY]
#Y = [i[1] for i in XY]

plt.figure(figsize=(8,8))
plt.axis("equal")
plt.fill([i[0] for i in XY], [i[1] for i in XY])
plt.savefig('koch_snowflake.png')
