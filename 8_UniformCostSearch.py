
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
        current = node[1][len(node[1]) - 1] # name of node

        if end in node[1]:  # if destination node found
            print("Path found: " + str(node[1]) + ", Cost = " + str(node[0]))
            break

        cost = node[0]
        for neighbor in graph[current]:
            temp = node[1][:]   # get the current node
            temp.append(neighbor)
            cost=cost + graph[current][neighbor] # total cost from 'temp' to 'neighbour'
            queue.put((cost, temp))
            print(current + "-" + neighbor,cost)


def readGraph():
    input_file=open("map_input.txt","r")
    lines=int(input_file.readline().split('\n')[0])
    graph = {}

    for line in range(lines):
        line=input_file.readline().split('\n')[0]
        #line = input()

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