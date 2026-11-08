# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        def count(node, largest):
            if node is None:
                return 0

            good = 1 if node.val >= largest else 0
            largest = max(largest, node.val)

            return good + count(node.left, largest) + count(node.right, largest)

        return count(root, root.val)
