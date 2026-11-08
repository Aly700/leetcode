# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


from collections import deque


class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        view = []
        queue = deque([root] if root else [])

        while queue:
            width = len(queue)
            for i in range(width):
                node = queue.popleft()
                if i == width - 1:
                    view.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

        return view
