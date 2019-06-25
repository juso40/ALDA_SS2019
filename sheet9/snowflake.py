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
        cos60 = math.cos(math.radians(60))#we will need cos and sin very often
        sin60 = math.sin(math.radians(60))  
        for _ in range(level):
            for i in range(len(coordinates)):

                p1 = coordinates[i] #get a third of our x/y of point1
                p1X = p1[0] / 3
                p1Y = p1[1] / 3

                if i == len(coordinates) - 1:   #get a third of our x/y of point2
                    p2 = coordinates[0]
                else:
                    p2 = coordinates[i+1]
                
                p2X = p2[0] / 3
                p2Y = p2[1] / 3

                third1 = (p1X + p1X + p2X, p1Y + p1Y + p2Y)#Third of the way from p1 to p2
                third2 = (p1X + p2X + p2X, p1Y + p2Y+ p2Y)#Two thirds from p1 to p2

                #only a temp vector variable
                vec2DX = third2[0] - third1[0]
                vec2DY = third2[1] - third1[1] 

                #rotate our temp vector by 60 degrees
                rotatedX = cos60 * vec2DX + sin60 * vec2DY
                rotatedY = -sin60 * vec2DX + cos60 * vec2DY

                #add the rotated vector on top of the first third, for the midpoint
                midpoint = (rotatedX + third1[0], rotatedY + third1[1])
            
                XY.extend((coordinates[i],
                            third1,
                            midpoint,
                            third2))
            coordinates = XY
        return XY
            
         
XY = kochSnowflake(9)
for i in XY:
    X = i[0]
    Y = i[1]

plt.figure(figsize=(8,8))
plt.axis("equal")
plt.fill(X, Y)
plt.savefig('koch_snowflake.png')
