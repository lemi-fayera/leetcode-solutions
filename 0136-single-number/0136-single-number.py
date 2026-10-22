class Solution:
    def singleNumber(self, nums: list[int]) -> int:
        count = Counter(nums)
        for num in count:
            if count[num] == 1:
                return num