# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        longest = 0

        def depth(node):
            nonlocal longest
            if node is None:
                return 0

            left = depth(node.left)
            right = depth(node.right)
            longest = max(longest, left + right)

            return 1 + max(left, right)

        depth(root)

        return longest
