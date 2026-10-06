from collections import Counter

class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        count = Counter(nums)

        sortedItem = sorted(
            count.items(),
            key=lambda x: x[1],
            reverse=True
        )

        topk = sortedItem[:k]

        return [x[0] for x in topk]
