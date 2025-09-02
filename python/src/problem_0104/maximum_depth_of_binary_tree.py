# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from utils.trees import TreeNode


class Solution:
    def maxDepth(self, root: TreeNode | None) -> int:
        """
        time: O(n)
        memory: O(n)
            - best case (balanced tree): O(log(n))
            - worst Case (degenerate tree): O(n)
        approach: recursive depth first search
        """
        if not root:
            return 0

        return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))
