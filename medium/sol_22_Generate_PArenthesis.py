from collections import deque
class S:

    def bribe(q):

        def get_neighbors(arr):
            pm = []
            for i in range(1,len(arr)):
                arr[i],arr[i-1] = arr[i-1], arr[i]
                pm.append(arr.copy())
                arr[i], arr[i - 1] = arr[i - 1], arr[i]
            return pm

        qu = deque()
        qu.append(list(range(1,len(q) + 1)))
        depth = 0
        while qu and depth < 2:
            depth +=1
            n = len(qu)
            for i in range(n):
                state = qu.popleft()
                neighbors = get_neighbors(state)
                for neighbor in neighbors:
                    if neighbor == q:
                        return 'possible'
                    else:
                        qu.append(neighbor)

        return 'not possible'






if __name__ == '__main__':
    S.bribe(q = [2, 1, 5, 3, 4])
    # print(S.bribe(q = [2, 5, 1, 3, 4]))
















if __name__ == '__main__':
    print(S.bribe(q = [2, 1, 5, 3, 4]))





















