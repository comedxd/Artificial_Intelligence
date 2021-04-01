import queue as Q
def uniform_cost_search(graph, start, end):
    if start not in graph:
        raise TypeError(str(start) + ' not found in graph !')
        return
    if end not in graph:
        raise TypeError(str(end) + ' not found in graph !')
        return
    queue = Q.PriorityQueue()
    queue.put((0, [start]))
    while not queue.empty():
        node = queue.get()
        current = node[1][len(node[1]) - 1]

        if end in node[1]:
            print("Path found: " + str(node[1]) + ", Cost = " + str(node[0]))
            break

        cost = node[0]
        for neighbor in graph[current]:
            temp = node[1][:]
            temp.append(neighbor)
            queue.put((cost + graph[current][neighbor], temp))


def readGraph():
    input_file=open("map_input.txt","r")
    lines=int(input_file.readline().split('\n')[0])
    graph = {}

    for line in range(lines):
        line=input_file.readline().split('\n')[0]
        tokens = line.split()
        node = tokens[0]
        graph[node] = {}

        for i in range(1, len(tokens) - 1, 2):
            #print(node, tokens[i], tokens[i + 1])
            graph[node][tokens[i]] = int(tokens[i + 1] )
    return graph


# driver code
if __name__=="__main__":
    graph = readGraph()
    uniform_cost_search(graph, 'Arad', 'Bucharest')