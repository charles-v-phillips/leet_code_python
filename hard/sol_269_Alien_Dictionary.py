from collections import defaultdict
class Solution:
    def alienOrder(self, words):
        # First we must make the graph
        g = defaultdict(set)
        indegree = defaultdict(int)
        for i in range(len(words) - 1):
            w1 = words[i]
            w2 = words[i + 1]
            shorter_word_length = len(min(w1,w2, key=len))

            j = 0
            while j < shorter_word_length :
                c1 = w1[j]
                c2 = w2[j]

                if c1 == c2:
                    j += 1
                else:
                    g[c1].add(c2)
                    indegree[c2] += 1
                    break

            if j == shorter_word_length:
                g[c1].add(c2)
                if w1 != w2:
                    indegree[c2] += 1

        top_order = []
        nodes_with_no_incoming_edges = []


        for node in g:
            if node not in indegree:
                nodes_with_no_incoming_edges.append(node)

        if not nodes_with_no_incoming_edges:
            return ""

        while nodes_with_no_incoming_edges:
            node = nodes_with_no_incoming_edges.pop()
            top_order.append(node)

            for neighbor in g[node]:
                indegree[neighbor] -= 1
                if indegree[neighbor] == 0:
                    nodes_with_no_incoming_edges.append(neighbor)


        return ''.join(top_order)

from collections import deque
class Solution2:
    def alienOrder(self, words):
        g = defaultdict(set)
        in_degree = {c: 0 for word in words for c in word}

        for word1, word2 in zip(words,words[1:]):
            for c1, c2 in zip(word1, word2):
                if c1 != c2:
                    if c2 not in g[c1]: #Even though we use a set here, we still need to check this condition to decide whether or nt to increase the indegree
                        g[c1].add(c2)
                        in_degree[c2] += 1
                    break
            else: # <-- Grade A Fuckery
                if len(word2) < len(word1): return ""

        # Kahns Algorithm for Topological Sorting
        output = []
        q = deque([c for c in in_degree if in_degree[c] == 0])
        while q:
            node = q.popleft()
            output.append(node)
            for neighbor in g[node]:
                in_degree[neighbor] -= 1
                if in_degree[neighbor] == 0:
                    q.append(neighbor)

        if len(output) != len(in_degree):
            return ""

        return "".join(output)
















if __name__ == '__main__':
    # print(Solution2().alienOrder(words = ["wrt","wrf","er","ett","rftt"]))
    # print(Solution().alienOrder(words=["z","z"]))
    # print(Solution2().alienOrder(words=["zy","zx"]))
    # print(Solution2().alienOrder(words=["ac","ab","zc","zb"]))
    for i in range(5):
        if 6 > i:
            print('impossible')
    else:
        print('hello')
