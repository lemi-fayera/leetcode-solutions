class Solution:
    def runningSum(self, nums: list[int]) -> list[int]:
        result = []
        sum = 0
        for num in nums:
            sum += num
            result.append(sum)
        return result