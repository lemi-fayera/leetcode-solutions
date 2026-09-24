class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals = [tuple(interval) for interval in intervals]
        intervals.sort()

        merged = []

        for start, end in intervals:
            if not merged or start > merged[-1][1]:
                merged.append((start, end))
            else:
                old_start, old_end = merged[-1]
                merged[-1] = (old_start, max(old_end, end))

        return merged