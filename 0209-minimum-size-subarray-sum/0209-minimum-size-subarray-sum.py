class Solution:
    def minSubArrayLen(self, target: int, nums: list[int]) -> int:
        arr = []
        s = 0
        min_len = float('inf')

        for i in range(len(nums)):
            arr.append(nums[i])
            s += nums[i]

            while s >= target:
                min_len = min(min_len, len(arr))
                s -= arr[0]
                arr.pop(0)

        return 0 if min_len == float('inf') else min_len