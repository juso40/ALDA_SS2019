from pgm import *

width, height, data = readPGM("cells.pgm")


def createMask(width, height, data, treshold):
    return [0 if value < treshold else 255 for value in data]

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

    def tryRight(pixel, right, tempList):
        if pixel == right:
            tempList.append(x + 1 + y * width)

    def tryLeft(pixel, left, tempList):
        if pixel == left:
            tempList.append(x - 1 + y * width)

    def tryUp(pixel, up, tempList):
        if pixel == up:
            tempList.append(x + (y - 1) * width)

    def tryDown(pixel, down, tempList):
        if pixel == down:
            tempList.append(x + (y + 1) * width)


    graph = []

    for index, pixel in enumerate(mask):
        x, y = index % width, index // width
        tempList = []
        Left = getLeft(x, y)
        Right = getRight(x, y)
        Up = getUp(x, y)
        Down = getDown(x, y)

        # oben links -> 2 nachbarn
        if x == 0 and y == 0:
            tryRight(pixel, Right, tempList)
            tryDown(pixel, Down, tempList)
        # unten links -> 2 nachbarn
        elif x == 0 and y == height - 1:
            tryRight(pixel, Right, tempList)
            tryUp(pixel, Up, tempList)
        # oben rechts -> 2 nachbarn
        elif x == width - 1 and y == 0:
            tryLeft(pixel, Left, tempList)
            tryDown(pixel, Down, tempList)
        # unten rechts -> 2 nachbarn
        elif x == width - 1 and y == height - 1:
            tryLeft(pixel, Left, tempList)
            tryUp(pixel, Up, tempList)
        # linke kante -> 3 nachbarn
        elif x == 0:
            tryRight(pixel, Right, tempList)
            tryUp(pixel, Up, tempList)
            tryDown(pixel, Down, tempList)
        # rechte kante -> 3 nachbarn
        elif x == width:
            tryLeft(pixel, Left, tempList)
            tryUp(pixel, Left, tempList)
            tryDown(pixel, Down, tempList)
        # top line -> 3 nachbarn
        elif y == 0:
            tryRight(pixel, Right, tempList)
            tryLeft(pixel, Left, tempList)
            tryDown(pixel, Down, tempList)
        # bottom line -> 3 nachbarn
        elif y == height - 1:
            tryRight(pixel, Right, tempList)
            tryLeft(pixel, Left, tempList)
            tryUp(pixel, Up, tempList)
        # rest -> 4 nachbarn
        else:
            tryRight(pixel, Right, tempList)
            tryLeft(pixel, Left, tempList)
            tryDown(pixel, Down, tempList)
            tryUp(pixel, Up, tempList)

        graph.append(tempList[:])
        tempList *= 0

    return graph


graph = createGraph(width, height, mask)


def findAnchor(anchors, node):
    start = node
    while node != anchors[node]:
        node = anchors[node]
    anchors[start] = node
    return node


def connectedComponents(graph):
    anchors = list(range(len(graph)))
    for node in range(len(graph)):
        for neighbor in graph[node]:
            if neighbor < node:
                continue
            a1 = findAnchor(anchors, node)
            a2 = findAnchor(anchors, neighbor)
            if a1 < a2:
                anchors[a2] = a1
            elif a2 < a1:
                anchors[a1] = a2
    labels = [None] * len(graph)
    current_label = 0
    for node in range(len(graph)):
        a = findAnchor(anchors, node)
        if a == node:
            labels[a] = current_label
            current_label += 1
        else:
            labels[node] = labels[a]
    return anchors, labels


anchors, labeling = connectedComponents(graph)

writePGM(width, height, labeling, "labeling.pgm")


def getSize(labeling):
    size = []
    helperList = []
    for label in labeling:
        if label not in helperList:
            size.append((label, labeling.count(label)))
            helperList.append(label)
    return size


size = getSize(labeling)


def getMaxIntensity(data, labeling):
    intensity = []
    helperList = []
    checkIndex = []
    for label in labeling:
        if label not in helperList:
            checkIndex.append([label, [i for i, x in enumerate(labeling) if x == label]])
            helperList.append(label)
    for temp in checkIndex:
        tempIntensity = []
        for index in temp[1]:
            tempIntensity.append(data[index])
        intensity.append([temp[0], max(tempIntensity)])
        tempIntensity.clear()
    return intensity


intensity = getMaxIntensity(data, labeling)


def createOutput(labeling, size, intensity):
    whiteTreshold = 220
    newData = []
    less_than_30 = [x[0] for x in size if x[1] < 30]
    white = [x[0] for x in intensity if x[1] > whiteTreshold]
    gray = [x[0] for x in intensity if x[1] <= whiteTreshold]

    for label in labeling:
        if label == 0:
            newData.append(0)
        elif label in less_than_30:
            newData.append(255)
        elif label in white:
            newData.append(160)
        elif label in gray:
            newData.append(80)
    return newData


newData = createOutput(labeling, size, intensity)

writePGM(width, height, newData, "output.pgm")
