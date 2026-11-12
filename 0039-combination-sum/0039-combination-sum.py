class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        result = []
        chosen = []

        def walk(start, remaining):
            if remaining == 0:
                result.append(chosen[:])
                return

            for i in range(start, len(candidates)):
                if candidates[i] > remaining:
                    continue
                chosen.append(candidates[i])
                walk(i, remaining - candidates[i])
                chosen.pop()

        walk(0, target)

        return result
