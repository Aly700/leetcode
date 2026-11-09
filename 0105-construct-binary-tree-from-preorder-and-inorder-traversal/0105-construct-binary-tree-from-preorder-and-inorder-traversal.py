# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        position = {value: i for i, value in enumerate(inorder)}
        next_root = 0

        def build(left, right):
            nonlocal next_root
            if left > right:
                return None

            value = preorder[next_root]
            next_root += 1

            node = TreeNode(value)
            node.left = build(left, position[value] - 1)
            node.right = build(position[value] + 1, right)

            return node

        return build(0, len(inorder) - 1)
