class Solution:
    def findCenter(self, edges) -> int:
        d = {}

        for edge in edges:
            if edge[0] not in d:
                d[edge[0]] =1
            if edge[1] not in d:
                d[edge[1]] = 1

            if edge[0] in d:
                d[edge[0]] +=1
            if edge[1] in d:
                d[edge[1]] += 1
            if d[edge[0]] >2:
                return edge[0]
            if d[edge[1]] > 2:
                return edge[1]







