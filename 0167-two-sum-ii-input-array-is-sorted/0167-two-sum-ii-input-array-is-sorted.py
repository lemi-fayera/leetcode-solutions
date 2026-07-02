class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left = 0
        right = len(numbers) - 1

        while left < right:
            istarget = numbers[left] + numbers[right]

            if istarget == target:
                return [left + 1, right + 1]
            elif istarget < target:
                left += 1
            else:
                right -= 1