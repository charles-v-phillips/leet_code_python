class Solution:
    def maxArea(self, height):
        n = len(height)

        l,r = 0, n-1
        tallest_left = height[l]
        tallest_right = height[n]
        largest_area = 0

        while l < r:
            height = min(tallest_left,tallest_right)
            dist = r - l
            area = height*dist
            largest_area = max(largest_area, area)
            if height[l] < height[r]:
                l += 1
            else:
                r -=1
        return largest_area

if __name__ == '__main__':
    pass





