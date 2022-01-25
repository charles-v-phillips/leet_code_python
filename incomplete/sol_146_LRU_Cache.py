from collections import deque,defaultdict
class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        l = deque()
        d = defaultdict()


    def get(self, key: int) -> int:
        pass

    def put(self, key: int, value: int) -> None:
        self.d[key] = value
        if len(self.d.keys()) > self.capacity:
            self.l.pop()


if __name__ == '__main__':
    pass

