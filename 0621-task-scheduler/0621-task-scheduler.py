class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        count = Counter(tasks)

        max_freq = max(count.values())

        max_count_tasks = 0
        for freq in count.values():
            if freq == max_freq:
                max_count_tasks += 1

        intervals = (max_freq - 1) * (n + 1) + max_count_tasks

        return max(len(tasks), intervals)