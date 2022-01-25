from collections import defaultdict
class Solution:
    def alienOrder(self, words):
        # g = defaultdict(set)
        # max_len = len(max(words,key=len))
        # for i in range(max_len):
        #     letters = [w[i] for w in words if i < len(w)]
        #     for i in range(len(letters)-1):
        #         if letters[i] != letters[i+1]:
        #             g[letters[i]].add(letters[i+1])
        # print(g)

        words = ['*' + word for word in words]
        d = defaultdict(list)
        for word in words:
            d[word[0]].append(word)
        print(d)

        def helper(d):
            pass

        # g = defaultdict(list)













if __name__ == '__main__':
    # Solution().alienOrder(words = ["wrt","wrf","er","ett","rftt"])
    for i in range(3000):
        print(chr(i))