from pgm import *
from collections import Counter
from datetime import datetime
import cProfile


def do_cprofile(func):
    def profiled_func(*args, **kwargs):
        profile = cProfile.Profile()
        try:
            profile.enable()
            result = func(*args, **kwargs)
            profile.disable()
            return result
        finally:
            profile.print_stats()
    return profiled_func


startTime = datetime.now()

width, height, data = readPGM("cells.pgm")



def createMask(width, height, data, threshold):
    return [0 if value < threshold else 255 for value in data]


mask = createMask(width, height, data, 60)
writePGM(width, height, mask, "masked.pgm")


def get_neighbours(width, height, data, index, value):
    neighbours = []
    if index + width < width * height and data[index + width] == value:
        neighbours.append(index + width)
    if (index + 1) % width != 0 and data[index + 1] == value:
        neighbours.append(index + 1)
    if (index - 1) % width != 0 and data[index - 1] == value:
        neighbours.append(index - 1)
    if index - width >= 0 and data[index - width] == value:
        neighbours.append(index - width)
    return neighbours

@do_cprofile
def createGraph(width, height, data):
    graph = []
    for index, element in enumerate(data):
        neighbours = get_neighbours(width, height, data, index, element)
        graph.append(neighbours)
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
    return list(Counter(labeling).values())


size = getSize(labeling)


def getMaxIntensity(data, labeling):
    max_label = max(labeling)
    intensities = [0] * (max_label + 1)
    for label, value in zip(labeling, data):
        if intensities[label] < value:
            intensities[label] = value
    return intensities


intensity = getMaxIntensity(data, labeling)


def createOutput(labeling, sizes, intensities):
    white_threshold = 220
    black_threshold = 60
    output = [0] * len(labeling)
    for index, label in enumerate(labeling):
        label = labeling[index]
        if sizes[label] < 30:
            output[index] = 255
        elif intensities[label] >= white_threshold:
            output[index] = 160
        elif intensities[label] >= black_threshold:
            output[index] = 80
    return output


newData = createOutput(labeling, size, intensity)

writePGM(width, height, newData, "output.pgm")
print(datetime.now() - startTime)
