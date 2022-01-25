import collections
class Solution:
    def findLadders(self, beginWord: str, endWord: str, wordList):
        rv = []
        n = len(beginWord)

        if endWord not in wordList or not wordList or not beginWord or not endWord:
            return rv

        all_combos = collections.defaultdict(list)

        for word in wordList:
            for i in range(n):
                all_combos[word[:i] + '*' + word[i+1:]].append(word)

        #BFS

        q = collections.deque([(beginWord, 1)])
        visited = {beginWord: True}
        came_from = []

        while q:
            word,depth = q.popleft()

            for i in range(n):
                partial_word = word[:i] + '*' + word[i+1:]
                for w in all_combos[partial_word]:
                    if w == endWord:
                        return depth + 1
                    if w not in visited:
                        visited[w] = True
                        q.append((w,depth + 1))
        return 0

class Solution2:
    def findLadders(self, beginWord: str, endWord: str, wordList):
        def dfs2(word,depth):
            if depth >= self.min_length:
                return
            if word == endWord:
                print("PATH FOUND")
                p = self.partial_path.copy()
                p.append(endWord)
                if len(p) < self.min_length:
                    self.min_length = len(p)
                    self.rv.clear()
                    self.rv.append(p)
                elif len(p) == self.min_length:
                    self.rv.append(p)


                return
            self.partial_path.append(word)
            for i in range(len(word)):
                partial = word[:i] + '*' + word[i+1:]
                if not self.visited[partial]:
                    self.visited[partial] = True
                    for w in self.all_combos[partial]:
                        if w != word : dfs2(w,depth  +1)
                    self.visited[partial] = False
            self.partial_path.pop()


        self.visited = {}
        self.rv = []
        self.partial_path = []
        self.min_length = float('inf')


        if endWord not in wordList or not wordList or not beginWord or not endWord:
            return self.rv

        if beginWord not in wordList:
            wordList.append(beginWord)

        self.all_combos = collections.defaultdict(list)

        for word in wordList:
            for i in range(len(word)):
                p = word[:i] + '*' + word[i + 1:]

                self.all_combos[p].append(word)
                self.visited[p] = False

        dfs2(beginWord,0)
        return self.rv

class Solution3:
    def findLadders(self, beginWord: str, endWord: str, wordList):
        visited = {}
        rv = []
        min_length = float('inf')

        if endWord not in wordList or not wordList or not beginWord or not endWord:
            return rv

        if beginWord not in wordList:
            wordList.append(beginWord)

        all_combos = collections.defaultdict(list)

        for word in wordList:

            for i in range(len(word)):
                visited[word] = False
                p = word[:i] + '*' + word[i + 1:]

                all_combos[p].append(word)



        #BFS

        q = collections.deque([([beginWord,[beginWord],0])])   # word,partial path, depth


        while q:
            l = len(q)
            for i in range(l):
                word,path,depth = q.popleft()
                if depth == min_length:
                    continue

                if word == endWord:

                    if len(path) < min_length:
                        rv.clear()
                        rv.append(path)
                    if len(p) == min_length:
                        rv.append(path)
                    continue

                for i in range(len(word)):

                    partial = word[:i] + '*' + word[i+1:]
                    if visited[word]:
                        continue

                    for w in all_combos[partial]:
                        if  w != word:
                            q.append((w,path + [w],depth + 1))
            visited[word] = True


        return rv







class Solution4:
    def findLadders(self, beginWord: str, endWord: str, wordList):
        wordList = set(wordList)
        res = []
        layer = {}
        layer[beginWord] = [[beginWord]]

        while layer:
            newlayer = collections.defaultdict(list)
            for w in layer:
                if w == endWord:
                    res.extend(k for k in layer[w])
                else:
                    for i in range(len(w)):
                        for c in 'abcdefghijklmnopqrstuvwxyz':
                            neww = w[:i] + c + w[i + 1:]
                            if neww in wordList:
                                newlayer[neww] += [j + [neww] for j in layer[w]]

            wordList -= set(newlayer.keys())
            layer = newlayer

        return res







if __name__ == '__main__':
    print(Solution4().findLadders(beginWord = "hit", endWord = "cog", wordList = ["hot","dot","dog","lot","log","cog"]))

