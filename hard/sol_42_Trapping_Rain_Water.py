from typing import List

class Solution2:
    @staticmethod
    def create_stacks_and_peaks(arr):
        peaks = []
        peaks.append([0,arr[0]])
        comp = min
        vtc = float('inf')
        i = 1
        while i < len(arr)-1:
            if comp(vtc, arr[i]) == arr[i]:
                vtc = comp(vtc, arr[i])
                i += 1
            else:
                if (arr[i-2] < arr[i-1]) and (arr[i-1] > arr[i]):
                    peaks.append([i,arr[i]])
                comp = min if comp == max else max
                vtc = 0 if comp == max else float('inf')
                i += 1


        peaks.append([len(arr) - 1, arr[-1]])
        return peaks

    @staticmethod
    def trim(arr):
        l, r = 0, len(arr) - 1
        maxi = 0

        while l < len(arr):

            if arr[l] >= maxi:
                maxi = arr[l]
                l += 1

            else:
                l -= 1
                break

        mini = 0
        while r >= 0:
            if arr[r] >= mini:
                mini = arr[r]
                r -= 1
            else:
                r += 1
                break
        return arr[l:r+1]

    @staticmethod
    def trap(height: List[int]) -> int:
        height= Solution2.trim(height)
        if not height:
            print('nope')
            return 0
        print(f'{len(height)=}')

        peaks = Solution2.create_stacks_and_peaks(height)
        print(f'{peaks=}')
        # l, r = 0
        # while l < len(m_s):



class Solution:
    def trap(self, height):
        def trim(arr):
            l, r = 0, len(arr) - 1
            maxi = 0

            while l < len(arr):

                if arr[l] >= maxi:
                    maxi = arr[l]
                    l += 1

                else:
                    l -= 1
                    break

            mini = 0
            while r >= 0:
                if arr[r] >= mini:
                    mini = arr[r]
                    r -= 1
                else:
                    r += 1
                    break
            return arr[l:r + 1]

        def find_peaks(arr):
            peaks = []
            peaks.append(0)
            comp, vtc = min, float('inf')
            i = 1
            while i < len(arr):
                if comp(vtc, arr[i]) == arr[i]:
                    vtc = arr[i]
                    i += 1
                else:
                    if comp == max:
                        peaks.append(i-1)
                    (comp, vtc) = (min, float('inf')) if comp == max else (max, 0)

            peaks.append(i-1)
            return peaks

        height = trim(height)
        if len(height) < 2:
            return 0
        peaks = find_peaks(height)
        print(f'{peaks=}')
        #
        # l = r = 0
        #  while r < len(height):
        #      while height[l]



class Solution:
    def trap(self, height):
        if not height:
            return 0

        l,r = 0, len(height) - 1
        l_max, r_max = height[l], height[r]
        tot = 0

        while l < r:
            if l_max < r_max:
                l += 1
                l_max = max(l_max, height[l])
                tot += l_max - height[l]
            else:
                r -= 1
                r_max = max(r_max, height[r])
                tot += r_max - height[r]
        return tot










if __name__ == '__main__':
    # print(Solution().trap([1,2,3,4,3,2,1,2,3,4,3,2,1,2,3,4,3,2,1]))
    # print(Solution().trap(height = [0,1,0,2,1,0,1,3,2,1,2,1]))
    print(Solution().trap(height = [4,2,0,3,2,5]))
    # print(Solution().trap([1,2,3,4,5,5,4,5,4,3,2,1]))