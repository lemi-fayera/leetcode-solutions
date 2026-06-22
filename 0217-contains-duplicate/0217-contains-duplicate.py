class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        newNums = set()

        for num in nums:
            if num in newNums:
                return True
            newNums.add(num)

        return False