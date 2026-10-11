class Solution:
    def maxProduct(self, nums: list[int]) -> int:
        nums.sort()
        max1 = nums[-1]
        max2 = nums[-2]
        return (max1 - 1) * (max2 - 1)