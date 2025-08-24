from utils.trees import TreeNode
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def searchBST(self, root: TreeNode | None, val: int) -> TreeNode | None:
        """
        time: O(log n)
        space: O(log n)
        approach: recursive
        """
        if not root:
            return None

        if root.val < val:
            return self.searchBST(root.right, val)
        if root.val > val:
            return self.searchBST(root.left, val)
        return root
