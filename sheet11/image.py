from pgm import *

width, height, data = readPGM("cells.pgm")


def createMask(width, height, data, treshold):
    for index, pixel in enumerate(data):
        if pixel <= treshold:
            data[index] = 0
    return data


mask = createMask(width, height, data, 60)

writePGM(width, height, mask, "masked.pgm")






def createGraph(width, height, mask):
    def getRight(x, y):
        if x != width - 1:
            return mask[x + 1 + y * width]

    def getLeft(x, y):
        return mask[x - 1 + y * width]

    def getUp(x, y):
        return mask[x + (y - 1) * width]

    def getDown(x, y):
        if y != height - 1:
            return mask[x + (y + 1) * width]
    
    #value = data[x + y*width]
    #data[x + y*width] = value
    #index = x + y*width
    #x, y = index % width, index // width
    
    graph = []

    for index, pixel in enumerate(mask):
        x, y = index % width, index // width
        tempList = []
        Left = getLeft(x, y)
        Right = getRight(x, y)
        Up = getUp(x, y)
        Down = getDown(x, y)

        #oben links -> 2 nachbarn
        if x == 0 and y == 0:
            if pixel != 0:
                if Right != 0:
                    tempList.append(Right)
                if Down != 0:
                    tempList.append(Down)
            else: 
                if Right == 0:
                    tempList.append(Right)
                if Down == 0:
                    tempList.append(Down)
            
        #unten links -> 2 nachbarn
        elif x == 0 and y == height - 1:
            if pixel != 0:
                if Right != 0:
                    tempList.append(Right)
                if Up != 0:
                    tempList.append(Up)
            else:
                if Right == 0:
                    tempList.append(Right)
                if Up == 0:
                    tempList.append(Up)

        #oben rechts -> 2 nachbarn
        elif x == width - 1 and y == 0:
            if pixel != 0:
                if Left != 0:
                    tempList.append(Left)
                if Down != 0:
                    tempList.append(Down)
            else:
                if Left == 0:
                    tempList.append(Left)
                if Down == 0:
                    tempList.append(Down)

        #unten rechts -> 2 nachbarn
        elif x == width - 1 and y == height - 1:
            if pixel != 0:
                if Left != 0:
                    tempList.append(Left)
                if Up != 0:
                    tempList.append(Up)
            else:
                if Left == 0:
                    tempList.append(Left)
                if Up == 0:
                    tempList.append(Up)

        #linke kante -> 3 nachbarn
        elif x == 0:
            pass
        #rechte kante -> 3 nachbarn
        elif x == width:
            pass
        #top line -> 3 nachbarn
        elif y == 0:
            pass
        #bottom line -> 3 nachbarn
        elif y == height-1:
            pass
        #rest -> 4 nachbarn
        else:
            pass
        #print("y=%s \n height= %s" %(y, height))
        graph.extend([tempList])
        print(tempList)

        tempList.clear()

    return graph

graph = createGraph(width, height, mask)

#print(graph)
