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
                    tempList.append(x + 1 + y * width)
                if Down != 0:
                    tempList.append(x + (y + 1) * width)
            else: 
                if Right == 0:
                    tempList.append(x + 1 + y * width)
                if Down == 0:
                    tempList.append(x + (y + 1) * width)
            
        #unten links -> 2 nachbarn
        elif x == 0 and y == height - 1:
            if pixel != 0:
                if Right != 0:
                    tempList.append(x + 1 + y * width)
                if Up != 0:
                    tempList.append(x + (y - 1) * width)
            else:
                if Right == 0:
                    tempList.append(x + 1 + y * width)
                if Up == 0:
                    tempList.append(x + (y - 1) * width)

        #oben rechts -> 2 nachbarn
        elif x == width - 1 and y == 0:
            if pixel != 0:
                if Left != 0:
                    tempList.append(x - 1 + y * width)
                if Down != 0:
                    tempList.append(x + (y + 1) * width)
            else:
                if Left == 0:
                    tempList.append(x - 1 + y * width)
                if Down == 0:
                    tempList.append(x + (y + 1) * width)

        #unten rechts -> 2 nachbarn
        elif x == width - 1 and y == height - 1:
            if pixel != 0:
                if Left != 0:
                    tempList.append(x - 1 + y * width)
                if Up != 0:
                    tempList.append(x + (y - 1) * width)
            else:
                if Left == 0:
                    tempList.append(x - 1 + y * width)
                if Up == 0:
                    tempList.append(x + (y - 1) * width)

        #linke kante -> 3 nachbarn
        elif x == 0:
            if pixel != 0:
                if Right != 0:
                    tempList.append(x + 1 + y * width)
                if Up != 0:
                    tempList.append(x + (y - 1) * width)
                if Down != 0:
                    tempList.append(x + (y + 1) * width)
            else:
                if Right == 0:
                    tempList.append(x + 1 + y * width)
                if Up == 0:
                    tempList.append(x + (y - 1) * width)
                if Down == 0:
                    tempList.append(x + (y + 1) * width)
        #rechte kante -> 3 nachbarn
        elif x == width:
            if pixel != 0:
                if Left != 0:
                    tempList.append(x - 1 + y * width)
                if Up != 0:
                    tempList.append(x + (y - 1) * width)
                if Down != 0:
                    tempList.append(x + (y + 1) * width)
            else:
                if Left == 0:
                    tempList.append(x - 1 + y * width)
                if Up == 0:
                    tempList.append(x + (y - 1) * width)
                if Down == 0:
                    tempList.append(x + (y + 1) * width)
        #top line -> 3 nachbarn
        elif y == 0:
            if pixel != 0:
                if Right != 0:
                    tempList.append(x + 1 + y * width)
                if Left != 0:
                    tempList.append(x - 1 + y * width)
                if Down != 0:
                    tempList.append(x + (y + 1) * width)
            else:
                if Right == 0:
                    tempList.append(x + 1 + y * width)
                if Left == 0:
                    tempList.append(x - 1 + y * width)
                if Down == 0:
                    tempList.append(x + (y + 1) * width)
        #bottom line -> 3 nachbarn
        elif y == height-1:
            if pixel != 0:
                if Right != 0:
                    tempList.append(x + 1 + y * width)
                if Left != 0:
                    tempList.append(x - 1 + y * width)
                if Up != 0:
                    tempList.append(x + (y - 1) * width)
            else:
                if Right == 0:
                    tempList.append(x + 1 + y * width)
                if Left == 0:
                    tempList.append(x - 1 + y * width)
                if Up == 0:
                    tempList.append(x + (y - 1) * width)
        #rest -> 4 nachbarn
        else:
            if pixel != 0:
                if Right != 0:
                    tempList.append(x + 1 + y * width)
                if Left != 0:
                    tempList.append(x - 1 + y * width)
                if Up != 0:
                    tempList.append(x + (y - 1) * width)
                if Down != 0:
                    tempList.append(x + (y + 1) * width)
            else:
                if Right == 0:
                    tempList.append(x + 1 + y * width)
                if Left == 0:
                    tempList.append(x - 1 + y * width)
                if Up == 0:
                    tempList.append(x + (y - 1) * width)
                if Down == 0:
                    tempList.append(x + (y + 1) * width)
        
        graph.append(tempList[:])
        tempList *= 0

    return graph

graph = createGraph(width, height, mask)


def findAnchor(anchors, node):
     start = node                   # wir merken uns den Anfang der Kette
     while node != anchors[node]:   # wenn node kein Anker ist
         node = anchors[node]       # ... verfolge die Ankerkette weiter
     # Pfadkompression: aktualisiere den Eintrag am Anfang der Kette
     anchors[start] = node
     return node

def connectedComponents(graph):
    # Initialisierung der property map: jeder Knoten ist sein eigener Anker
    anchors = list(range(len(graph)))

    for node in range(len(graph)):     # iteriere über alle Knoten
        for neighbor in graph[node]:   # ... und über deren ausgehende Kanten
            if neighbor < node:        # ignoriere Kanten, die in falscher Richtung verlaufen
                continue
            # hier landen wir für jede Kante des Graphen genau einmal
            a1 = findAnchor(anchors, node)       # finde Anker ...
            a2 = findAnchor(anchors, neighbor)   # ... der beiden Endknoten
            if a1 < a2:                          # Verschmelze die beiden Teilgraphen
                # (verwende den kleineren der beiden Anker als Anker des
                anchors[a2] = a1
            elif a2 < a1:  # entstehenden Teilgraphen. Falls node und neighbor
                # den gleichen Anker haben, waren sie bereits im gleichen
                anchors[a1] = a2
                #  Teilgraphen, und es passiert hier nichts.)
    # Bestimme jetzt noch die Labels der Komponenten
    # Initialisierung der property map für Labels
    labels = [None]*len(graph)
    current_label = 0                  # die Zählung beginnt bei 0
    for node in range(len(graph)):
        # wegen der Pfadkompression zeigt jeder Knoten jetzt direkt auf seinen Anker
        a = findAnchor(anchors, node)
        if a == node:                  # node ist ein Anker
            labels[a] = current_label  # => beginne eine neue Komponente
            current_label += 1         # und zähle Label für die nächste ZK hoch
        else:
            # node ist kein Anker => setzte das Label des Ankers
            labels[node] = labels[a]
            # (wir wissen, dass labels[a] bereits gesetzt ist, weil
            #  der Anker immer der Knoten mit der kleinsten Nummer ist)
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
            checkIndex.append([label,[i for i, x in enumerate(labeling) if x == label]])
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
    whiteTreshold = 150
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