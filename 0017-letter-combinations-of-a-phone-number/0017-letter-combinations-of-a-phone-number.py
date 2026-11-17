class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []

        letters = {"2": "abc", "3": "def", "4": "ghi", "5": "jkl", "6": "mno", "7": "pqrs", "8": "tuv", "9": "wxyz"}
        combinations = [""]
        for digit in digits:
            combinations = [prefix + ch for prefix in combinations for ch in letters[digit]]

        return combinations
