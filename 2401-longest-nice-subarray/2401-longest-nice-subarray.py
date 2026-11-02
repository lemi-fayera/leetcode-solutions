class Solution:
    def longestNiceSubarray(self, nums: List[int]) -> int:
        left = 0
        used = 0
        max_length = 0

        for right in range(len(nums)):
            while used & nums[right]:
                used ^= nums[left]
                left += 1

            used |= nums[right]

            max_length = max(max_length, right - left + 1)

        return max_length
