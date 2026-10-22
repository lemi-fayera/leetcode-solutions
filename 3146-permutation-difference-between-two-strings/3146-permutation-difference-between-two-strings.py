class Solution:
    def findPermutationDifference(self, s: str, t: str) -> int:
        total = 0
        for char in s:
            total += abs(s.index(char) - t.index(char))

        return total