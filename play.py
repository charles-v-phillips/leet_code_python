import random
import heapq
def create_graph():
    g = {}

    with open("tiny.txt","r") as file:
        n = int(file.readline())
        for i in range(n):
            g[i] = {}
        file.readline()

        for line in file:
            strip = line.split()
            g[int(strip[0])][int(strip[1])] = int(float(strip[2])*100)
    file.close()
    return g






def dijkstra(graph,src,dst):
    def relax(node):
        for neighbor in graph[node]:
            if dist_to[neighbor] > dist_to[node] + graph[node][neighbor]:
                dist_to[neighbor] = dist_to[node] + graph[node][neighbor]
                heapq.heappush(h,(dist_to[neighbor],neighbor))


    dist_to = [float('inf') for _ in range(len(graph))]
    dist_to[src] = 0

    h = []
    heapq.heappush(h,(0,src))
    while len(h) != 0:
        node = heapq.heappop(h)[1]
        relax(node)

    for i in range(len(dist_to)):
        print("Distance from {} to {} is : {} ".format(src,i,dist_to[i]))





if __name__ == '__main__':
    dijkstra(create_graph(),0,7)


