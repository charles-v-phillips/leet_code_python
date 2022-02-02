import inspect
from dataclasses import dataclass
from functools import total_ordering
from typing import List
from pprint import pprint
import heapq


class MaxPQ:
    def __init__(self,capacity):
        self.__pq = [None]*(capacity  +1)
        self.__N = 0
    def swap(self,i,j):
        self.__pq[i], self.__pq[j] = self.__pq[j], self.__pq[i]

    def insert(self, x : int) -> None:
        self.__N += 1
        self.__pq[self.__N] = x
        self.swim(self.__N)

    def swim(self, k : int) -> None:
        while k > 1 and self.__pq[k] > self.__pq[k//2]:
            self.swap(k, k//2)
            k = k//2

    def sink(self, k : int) -> None:

        while 2*k <= self.__N:
            j = 2*k
            if j < self.__N and self.__pq[j] < self.__pq[j+1]:
                j += 1
            if self.__pq[k] >= self.__pq[j]:
                break
            self.swap(k,j)
            k = j


    def delMax(self):

        m = self.__pq[1]

        self.swap(1, self.__N)
        self.__N -= 1
        self.sink(1)
        return m







class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        pq = MaxPQ(len(nums))
        for e in nums:
            pq.insert(e)
        print('here')
        print(pq.delMax())
        print(pq.delMax())
        print(pq.delMax())
        print(pq.delMax())




# Solution().findKthLargest([1,5,23,45,76,23,65,44,33,37,81],3)


@dataclass(frozen=True,order=True)
class C:
    name : str

names = ['Charles', 'Jung', 'Tony', 'Hugh', 'Nicole']
c = [C(name) for name in names]

Solution().findKthLargest(c,4)


