class Solution:
    def intersection(self, nums1: list[int], nums2: list[int]) -> list[int]:
        inter = []
        for num in nums1:
            if num in nums2 and num not in inter:
                inter.append(num)
        return inter
