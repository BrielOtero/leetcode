from utils.trees import TreeNode

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def maxPathSum(self, root: TreeNode | None) -> int:
        """
        time: O(n)
        space: O(n)
        approach: depth first search
        """
        if not root:
            return 0

        res = root.val

        def dfs(node: TreeNode | None) -> int:
            nonlocal res

            if not node:
                return 0

            max_left = max(dfs(node.left), 0)
            max_right = max(dfs(node.right), 0)
            res = max(res, max_left + node.val + max_right)
            return node.val + max(max_left, max_right)

        dfs(root)

        return res
