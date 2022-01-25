class Solution:
    def search(self, nums, target) -> int:
        def find_pivot(l, r):
            if nums[l] <= nums[r-1]:
                return 0
            while l < r:
                pivot = (l + r) // 2

                if nums[pivot] == target:
                    return pivot
                else:
                    if nums[pivot] < nums[l]:
                        r = pivot - 1
                    else:
                        l = pivot + 1
        return find_pivot(0,len(nums))

if __name__ == '__main__':
    print(Solution().search(nums = [4,5,6,7,8,0], target = 4))