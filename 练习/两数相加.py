class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        d = {}
        for i , num in enumerate(nums):
            some = target - num
            if some in d:
                return [d[some], i]
            d[num] = i

s = Solution()
print(s.twoSum([2, 7, 11, 15], 9))