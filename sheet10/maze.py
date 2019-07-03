from time import sleep
graph = [
    [1],  # 00
    [3, 2, 0],  # 01
    [1],  # 02
    [5, 4, 1],  # 03
    [3],  # 04
    [7, 6, 3],  # 05
    [5],  # 06
    [10, 8, 5],  # 07
    [10, 9, 7],  # 08
    [8],  # 09
    [11, 8, 7],  # 10
    [13, 12, 10],  # 11
    [11],  # 12
    [15, 14, 11],  # 13
    [13],  # 14
    [13]  # 15
]

start = int(input("Enter the Startnode (0-15): "))
end = int(input("Enter the Targetnode (0-15): "))


def way_out(graph, startnode, targetnode, bDebug=False):
    visited = [False] * len(graph)
    deadends = []
    path = []

    def walk(node, targetnode, bDebug=False):
        if bDebug:
            input("Press \'ENTER\' for next step")
            print("On Node: %s" % node)
            for neighbor in graph[node]:
                print("My neighborse are %s, visited? %s" %
                      (neighbor, visited[neighbor]))

        if node == targetnode:  # target condition
            path.append(node)
            print("target reached!")
            print("Walked in %s dead ends!" % len(deadends))
            return True

        elif visited[node]:  # when already visited we need to backtrack
            print("%s backtracked" % node)
            path.append(node)

            if all(visited[i] for i in graph[node]):
                #print("Visited all connected nodes, go to the smallest one!!!")
                walk(graph[node][-1], targetnode, bDebug)
            else:
                for i in graph[node]:  # search the next not visited node
                    if not visited[i]:
                        walk(i, targetnode, bDebug)
                        break

        elif not visited[node]:  # we are on a not visited node
            path.append(node)
            if len(graph[node]) == 1:  # if this node only leads to one node it means
                visited[node] = True  # we are in a dead end
                deadends.append(node)
                print("%s dead end!" % node)
                walk(graph[node][0], targetnode, bDebug)
            else:
                visited[node] = True
                print("%s visited" % node)
                for neighbor in graph[node]:
                    if not visited[neighbor]:
                        walk(neighbor, targetnode, bDebug)
                        break

    walk(startnode, targetnode, bDebug)
    return path


path = way_out(graph, start, end)


def way_out_stack(graph, startnode, endnode):
    visited = [False] * len(graph)
    last_visited = []
    path = []
    deadends = 0

    current_node = startnode

    while current_node != endnode:
        if not visited[current_node]:
            path.append(current_node)
            last_visited.append(current_node)
            visited[current_node] = True
            if len(graph[current_node]) == 1:
                deadends += 1
                print("%s deadend!" % current_node)
            else:
                print("%s visited" % current_node)

        else:
            current_node = last_visited.pop()
            # path.append(current_node)
            print("Backtracked to %s" % current_node)

        for neighbor in graph[current_node]:
            if not visited[neighbor]:
                current_node = neighbor
                break

    print("Targetnode reached!!!")
    path.append(current_node)
    return path


stack_path = way_out_stack(graph, start, end)

print(path)
print(stack_path)

assert path==stack_path
print("Assert passed")
