import heapq
from typing import List

def getPrice(X,Y):
    if X == 'A' and Y == 'B':
        return 1
    if X == 'B' and Y == 'A':
        return -1
    if X == 'A' and Y == 'C':
        return 4
    if X == 'C' and Y == 'A':
        return -1
    if X == 'B' and Y == 'C':
        return 2
    if X == 'C' and Y == 'B':
        return -1
def getCheapestPrice(X: str, Y: str, cities: List[str]) -> int:
    def relax(node):
        for neighbor in cities:
            # here we check if there is a connection between the node and the neighbor
            price = getPrice(node, neighbor)
            if neighbor != node and price != -1:
                # If the oldest cheapest path is more expensive than the one we have just found, reassign the dist_to[city] to the cheaper path
                if price_to[neighbor] > price_to[node] + price:
                    price_to[neighbor] = price_to[node] + price
                    heapq.heappush(heap, (price_to[city], neighbor))

    # To find the cheapest path (shortest path), we will use Dijkstras Algorithm

    # First We initalize a dictionary to hold the price of the cheapest path found so far, and initialize every entry to infinity, except for our source city, which is initialized to be 0
    price_to = {city: float('inf') for city in cities}
    price_to[X] = 0

    # To efficiently relax all the nodes, we will use a priority queue to quickly access the city with highest priority, and push the starting city onto the heap
    heap = []
    heapq.heappush(heap, (0, X))

    # while we still have cities to consider, we will continually relax those nodes until there is nothing left ot relax
    while heap:
        city = heapq.heappop(heap)[1]
        relax(city)

    return price_to[Y]

print(getCheapestPrice('A','C',['A','B','C']))