import matplotlib.pyplot as plt
import math
from math import sqrt

def kochSnowflake(level):
    coordinates = [
                    (0, 0),
                    (1, 0),
                    (1/2, sqrt(3)/2)
                  ]
    if level == 0:
        return coordinates
    else:
        XY = []
        for _ in range(level):
            for i in range(len(coordinates)):

                p1 = coordinates[i]
                p1X = p1[0] / 3
                p1Y = p1[1] / 3

                p2 = coordinates[(i+1) % len(coordinates)]
                p2X = p2[0] / 3
                p2Y = p2[1] / 3

                third1 = (2 * p1X + p2X, 2 * p1Y + p2Y)
                third2 = (p1X + 2 * p2X, p1Y + 2 * p2Y)

                vec2DX = third2[0] - third1[0]
                vec2DY = third2[1] - third1[1] 

                cos60 = math.cos(math.radians(60))
                sin60 = math.sin(math.radians(60))
                
                rotatedX = cos60 * vec2DX + sin60 * vec2DY
                rotatedY = -sin60 * vec2DX + cos60 * vec2DY

                midpoint = (rotatedX + third1[0], rotatedY + third1[1])
            
                XY.extend((coordinates[i],
                            third1,
                            midpoint,
                            third2))
            coordinates = XY
        return XY
            
         
XY = kochSnowflake(9)
#X = [i[0] for i in XY]
#Y = [i[1] for i in XY]

plt.figure(figsize=(8,8))
plt.axis("equal")
plt.fill([i[0] for i in XY], [i[1] for i in XY])
plt.savefig('koch_snowflake.png')
