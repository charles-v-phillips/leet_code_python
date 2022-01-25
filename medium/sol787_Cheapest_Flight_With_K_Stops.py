import heapq
import collections
class Solution:
    def findCheapestPrice(self, n: int, flights: list, src: int, dst: int, k: int) -> int:
        visited = [False for _ in range(n)]
        path = []

        def dfs2(city,num_steps):

            if city == dst:

                return 0

            if (city,num_steps) in self.memo:
                return self.memo[(city,num_steps)]

            path.append(city)
            print("ADD : {}".format(path))


            visited[city] = True
            min_val = float('inf')
            for neighbor in self.g[city]:
                if not visited[neighbor] and num_steps < k+1:
                    min_val = min(min_val, self.g[city][neighbor] + dfs2(neighbor,num_steps+1))

            path.remove(city)
            print("REMOVE : {}   MIN VAL {}".format(path,min_val))
            self.memo[(city,num_steps)] = min_val
            visited[city] = False
            return min_val

        def dfs3(city, running_total, depth):
            if city == dst:
                self.min_val = running_total

            visited[city] = True

            for neighbor in self.g[city]:
                if not visited[neighbor] and running_total + self.g[city][neighbor] < self.min_val and depth < k+1:
                    dfs3(neighbor,running_total + self.g[city][neighbor],depth + 1)

            visited[city] = False




        self.g = {}
        self.memo = {}
        self.min_val = float('inf')
        for i in range(n):
            self.g[i] = {}
        for flight in flights:
            self.g[flight[0]][flight[1]] = flight[2]

        # val = dfs2(src,0)
        # return val if val < float('inf') else -1

        dfs3(src,0,0)
        return self.min_val

class Solution2:
    def findCheapestPrice(self, n: int, flights: list, src: int, dst: int, k: int) -> int:
        graph = collections.defaultdict(dict)
        for s, d, w in flights:
            graph[s][d] = w

        pq = [(0,src,0)]
        while pq:
            cost, node,steps = heapq.heappop(pq)
            if node == dst:
                return cost

            if steps == k+1:
                continue
            for neighbor, weight in graph[node].items():
                heapq.heappush(pq,(weight + cost,neighbor,steps  + 1))


        return -1



if __name__ == '__main__':
    print(Solution2().findCheapestPrice(5,
[[0,1,100],[0,2,100],[0,3,10],[1,2,100],[1,4,10],[2,1,10],[2,3,100],[2,4,100],[3,2,10],[3,4,100]],
0,
4,
3))