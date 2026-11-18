class Solution:
    def partition(self, s: str) -> List[List[str]]:
        n = len(s)
        palindrome = [[False] * n for _ in range(n)]
        for left in range(n - 1, -1, -1):
            for right in range(left, n):
                palindrome[left][right] = s[left] == s[right] and (right - left < 2 or palindrome[left + 1][right - 1])

        result = []
        parts = []

        def split(start):
            if start == n:
                result.append(parts[:])
                return
            for end in range(start, n):
                if palindrome[start][end]:
                    parts.append(s[start:end + 1])
                    split(end + 1)
                    parts.pop()

        split(0)
        return result
