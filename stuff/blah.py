def maxArea(height):
    l, r = 0, len(height) - 1
    max_area = 0

    while l < r:
        min_height = min(height[l], height[r])
        distance = r - l
        area = min_height * distance
        max_area = max(max_area, area)
        if height[l] < height[r]:
            l += 1
        else:
            r -= 1
    return max_area

print(maxArea([2,3,4,5,18,17,6]))
