from typing import List
class Solution:
    @staticmethod
    def findRLEArray(encoded1: List[List[int]], encoded2: List[List[int]]) -> List[List[int]]:
        def decompress(encoded):
            rv = []
            for val, reps in encoded:
                rv.extend([val]*reps)
            return rv


        def compress(raw):
            rv = []
            count = 1
            for i in range(len(raw) - 1):
                if raw[i] == raw[i+1]:
                    count += 1
                else:
                    rv.append([raw[i],count])
                    count = 1
            rv.append([raw[-1],count])
            return rv

        decoded1 = decompress(encoded1)
        decoded2 = decompress(encoded2)
        rv = []
        for v1,v2 in zip(decoded1,decoded2):
            rv.append(v1*v2)
        return compress(rv)

class Solution2:
    @staticmethod
    def findRLEArray(encoded1: List[List[int]], encoded2: List[List[int]]) -> List[List[int]]:
        p1 = p2 = 0
        rv = []
        placement1 = encoded1[0][1]
        placement2 = encoded2[0][1]

        while p1 < len(encoded1) or p2 < len(encoded2):
            e1 = encoded1[p1]
            e2 = encoded2[p2]

            overlap = min(e1[1],e2[1])
            to_append = [e1[0]*e2[0],overlap]
            if rv and rv[-1][0] == to_append[0]:
                rv[-1][1] += to_append[1]
            else:
                rv.append(to_append)

            if placement1 < placement2:
                p1 += 1
                placement1 += e1[1]

            elif placement1 > placement2:
                p2 += 1
                placement2 += e2[1]

            else:
                placement1 += e1[1]
                placement2 += e2[1]
                p1 += 1
                p2 += 1

        return rv

class Solution3:
    @staticmethod
    def findRLEArray(encoded1: List[List[int]], encoded2: List[List[int]]) -> List[List[int]]:
        p1 = p2 = 0
        rv = []
        while p1 < len(encoded1) and p2 < len(encoded2):
            e1_val, e1_freq = encoded1[p1]
            e2_val, e2_freq = encoded2[p2]

            overlap = min(e1_freq,e2_freq)
            encoded1[p1][1] -= overlap
            encoded2[p2][1] -= overlap

            to_insert = [e1_val * e2_val, overlap]

            if rv and rv[-1][0] == to_insert[0]:
                rv[-1][1] += overlap
            else:
                rv.append(to_insert)

            if encoded1[p1][1] == 0:
                p1 +=1
            if encoded2[p2][1] == 0:
                p2 += 1
        return rv




if __name__ == '__main__':
    print(Solution3.findRLEArray(encoded1 = [[1,3],[2,3]], encoded2 = [[6,3],[3,3]]))
    print(Solution3.findRLEArray([[2,3],[3,1]],[[1,1],[2,2],[3,1]]))
    print(Solution3.findRLEArray([[1,3],[2,1],[3,2]], [[2,3],[3,3]])) #[[2,3],[6,1],[9,2]]
