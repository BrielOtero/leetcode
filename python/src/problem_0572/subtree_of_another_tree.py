# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from utils.trees import TreeNode

class Solution:
    def isSubtree(self, root: TreeNode | None, subRoot: TreeNode | None) -> bool:  # noqa: N803
        """
        time: O(n^2)
        space: O(n)
        approach: depth first search
        """

        if not subRoot:
            return True
        if not root:
            return False

        if self.sameTree(root, subRoot):
            return True

        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)

    def sameTree(self, root: TreeNode | None, subRoot: TreeNode | None) -> bool:  # noqa: N803
        if not root and not subRoot:
            return True

        if root and subRoot and root.val == subRoot.val:
            return self.sameTree(root.left, subRoot.left) and self.sameTree(
                root.right, subRoot.right
            )

        return False
