from collections import Counter


class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        counts = Counter(tasks)
        most = max(counts.values())
        ties = sum(1 for count in counts.values() if count == most)

        return max(len(tasks), (most - 1) * (n + 1) + ties)
