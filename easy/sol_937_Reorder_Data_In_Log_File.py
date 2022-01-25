class Solution:
    def reorderLogFiles(self, logs) :
        letters = list(filter(lambda x : isinstance(x,(str,chr)),logs))
        numbers = list(filter(lambda x : isinstance(x,(int,float)),logs))
        print(letters,numbers)

if __name__ == '__main__':
    Solution().reorderLogFiles(["dig1 8 1 5 1","let1 art can","dig2 3 6","let2 own kit dig","let3 art zero"])

