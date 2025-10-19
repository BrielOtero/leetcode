from utils.trees import TreeNode

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Codec:
    """
    time: O(n)
    space: O(n)
    approach: depth first search
    """

    def serialize(self, root: TreeNode | None) -> str:
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """

        res: list[str] = []

        def dfs(node: TreeNode | None) -> None:
            if not node:
                res.append("null")
                return

            res.append(str(node.val))
            dfs(node.left)
            dfs(node.right)

        dfs(root)

        return ",".join(res)

    def deserialize(self, data: str) -> TreeNode | None:
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """

        vals = data.split(",")
        self.i = 0

        def dfs() -> TreeNode | None:
            if vals[self.i] == "null":
                self.i += 1
                return None

            node = TreeNode(int(vals[self.i]))
            self.i += 1

            node.left = dfs()
            node.right = dfs()

            return node

        return dfs()


# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))
