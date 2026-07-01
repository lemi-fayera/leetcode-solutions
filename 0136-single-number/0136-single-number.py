class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        n = {}

        for num in nums:
            n[num] = n.get(num, 0) + 1

        for num in nums:
            if n[num] == 1:
                return num