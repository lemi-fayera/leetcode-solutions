class Solution:
    def sortedSquares(self, nums: list[int]) -> list[int]:
        square = []
        for num in nums:
            square.append(num*num)
        return sorted(square)

        