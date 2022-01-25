from collections import defaultdict
class Trie:
    def __init__(self):
        self.children = {}

    def insert(self, word: str) -> None:
        t = self.children
        for c in word:
            if c in t:
                t = t[c]
            else:
                t[c] = {}
                t = t[c]
        t['*'] = '*'



    def countWordsEqualTo(self,word: str):
        pass

    def search(self, word: str) -> bool:
        t = self.children
        for c in word:
            if c in t:
                t = t[c]
            else:
                return False
        return '*' in t


    def startsWith(self, prefix: str) -> bool:
        if not prefix:
            return False
        t = self.children
        for c in prefix:
            if c not in t:
                return False
            t = t[c]
        return True

    def get_words(self):
        rv = []
        def helper(partial, d):
            if '*' in d:
                rv.append(partial)

            for c in d:
                if c != '*':
                    helper(partial + c, d[c])
        helper('',self.children)
        return rv





if __name__ == '__main__':
    trie = Trie()
    trie.insert('app')
    trie.insert('ore')
    trie.insert('apple')
    print(trie.get_words())


