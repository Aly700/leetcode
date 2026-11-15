class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        result = []
        chosen = []

        def search(start, remaining):
            if remaining == 0:
                result.append(chosen[:])
                return

            for i in range(start, len(candidates)):
                value = candidates[i]
                if value > remaining:
                    break
                if i > start and value == candidates[i - 1]:
                    continue
                chosen.append(value)
                search(i + 1, remaining - value)
                chosen.pop()

        search(0, target)
        return result
