from collections import OrderedDict

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.d = OrderedDict()

    def get(self, key: int) -> int:
        rv = self.d.get(key)
        if rv is not None:
            self.d.move_to_end(key)
            return rv

        return -1

    

    def put(self, key: int, value: int) -> None:
        if key in (self.d):
            self.d[key] = value
            self.d.move_to_end(key)
        
        elif len(self.d) < self.capacity:
                self.d[key] = value
        else:
            self.d.popitem(last=False)
            self.d[key] = value

        


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)

if __name__ == "__main__":
    cache = LRUCache(2)
    methods = [ "put", "put", "get", "put", "get", "put", "get", "get", "get"]
    params = [[1, 1], [2, 2], [1], [3, 3], [2], [4, 4], [1], [3], [4]]
    rv = [None]
    for (m,p) in zip(methods,params):
        s = (m  + str(tuple(p))  )
        rv.append(eval("cache." + s))
    print(rv)

    
