# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from utils.trees import TreeNode

class Solution:
    def isSameTree(self, p: TreeNode | None, q: TreeNode | None) -> bool:
        """
        time: O(n)
        space: O(n)
            - best case (balanced tree): O(log(n))
            - worst Case (degenerate tree): O(n)
        approach: depth first search, recursive
        """

        if not p and not q:
            return True

        if p and q and p.val == q.val:
            return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)

        return False
