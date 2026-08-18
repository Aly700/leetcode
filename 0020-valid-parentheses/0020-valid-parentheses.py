class Solution:
    def isValid(self, s: str) -> bool:

        stack = []
        closing = {')','}',']'}

        for parentheses in s:

            if parentheses in closing:

                if not stack:
                    return False

                popped = stack.pop()

                if not ((parentheses == ')' and popped == '(') or (parentheses == '}' and popped == '{') or (parentheses == ']' and popped == '[')):
                    return False

            else:

                stack.append(parentheses)

        return len(stack) == 0

        