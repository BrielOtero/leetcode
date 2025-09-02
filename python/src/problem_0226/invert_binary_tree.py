# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from utils.trees import TreeNode


class Solution:
    def invertTree(self, root: TreeNode | None) -> TreeNode | None:
        """
        time: O(n)
        space: O(n)
        approach: depth first search
        """

        if not root:
            return None

        root.left, root.right = root.right, root.left
        self.invertTree(root.left)
        self.invertTree(root.right)

        return root
