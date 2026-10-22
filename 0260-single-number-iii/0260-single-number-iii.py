class Solution:
    def singleNumber(self, nums: list[int]) -> list[int]:
        two_nums = []
        count = Counter(nums)
        for num in count:
            if count[num] == 1:
                two_nums.append(num)
        return two_nums
