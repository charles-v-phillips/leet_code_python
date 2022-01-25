from collections import defaultdict

# REPLACE MUTABLE DEFAULT ARGUMENT
class Node:
    def __init__(self, char=None, children=defaultdict(lambda : None)):
        self.char = char
        self.children = children
class Trie:


    def __init__(self, node =Node('*')):
        self.root = node

    def insert(self, word: str) -> None:
        traverser = self.root
        for c in word:
            if traverser.children[c]:
                traverser = traverser.children[c]
            else:
                insert = Node(c)
                traverser.children[c] = insert
                traverser = insert
        print('here')




    def search(self, word: str) -> bool:
        pass

    def startsWith(self, prefix: str) -> bool:
        pass



if __name__ == '__main__':
    trie = Trie()
    trie.insert('charles')
    print('here')
