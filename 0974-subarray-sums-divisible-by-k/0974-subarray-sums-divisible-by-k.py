class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        count = {0: 1}
        prefix_sum = 0
        result = 0

        for num in nums:
            prefix_sum += num

            remainder = prefix_sum % k

            result += count.get(remainder, 0)

            count[remainder] = count.get(remainder, 0) + 1

        return result