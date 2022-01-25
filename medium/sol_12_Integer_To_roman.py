class Solution:
    def intToRoman(self, num: int) -> str:
        d = {
             1: 'I',
             5: 'V',
             10:'X',
             50: 'L',
             100: 'C',
             500: 'D',
             1000: 'M'
        }
        rv = ''
        # num = str(num)
        # n = len(num)
        # i = len(str(int))-2
        # while num:
        #     bulk = num - (num % 10**i)
        #     closest_to = min(d.keys(), key =lambda x: abs(x - num))
        #     if closest_to in d:





        if num >= 1000:
            bulk = num - (num % 1000)
            rv += d[1000]*int((bulk/1000))
            num -= bulk










if __name__ == '__main__':
    print(Solution().intToRoman(1994))
