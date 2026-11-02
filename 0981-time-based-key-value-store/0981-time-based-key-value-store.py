from bisect import bisect_right
from collections import defaultdict


class TimeMap:
    def __init__(self):
        self.times = defaultdict(list)
        self.values = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.times[key].append(timestamp)
        self.values[key].append(value)

    def get(self, key: str, timestamp: int) -> str:
        times = self.times.get(key)
        if not times:
            return ""

        i = bisect_right(times, timestamp)
        if i == 0:
            return ""

        return self.values[key][i - 1]
