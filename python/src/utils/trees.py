from __future__ import annotations


class TreeNode:
    def __init__(
        self,
        val: int = 0,
        left: TreeNode | None = None,
        right: TreeNode | None = None,
    ):
        self.val = val
        self.left = left
        self.right = right


def create_tree_node(nodes: list[int | None] | None) -> TreeNode | None:
    """
    Build a binary tree from a list representation.

    Args:
        nodes: List representation of a binary tree where None represents empty nodes

    Returns:
        TreeNode: Root of the constructed binary tree

    Example:
        build_tree([4, 2, 7, 1, 3]) creates:
            4
           / \\
          2   7
         / \\
        1   3

    See also:
        serialize_tree: Function to convert a tree back to list representation
    """
    if not nodes or nodes[0] is None:
        return None

    root = TreeNode(nodes[0])  # type: ignore
    queue = [root]
    i = 1

    while queue and i < len(nodes):
        node = queue.pop(0)

        # Add left child
        if i < len(nodes) and nodes[i] is not None:
            node.left = TreeNode(nodes[i])  # type: ignore
            queue.append(node.left)
        i += 1

        # Add right child
        if i < len(nodes) and nodes[i] is not None:
            node.right = TreeNode(nodes[i])  # type: ignore
            queue.append(node.right)
        i += 1

    return root


def serialize_tree(root: TreeNode | None) -> list[int | None]:
    """
    Convert a binary tree to its level-order list representation.
    This matches the format used by LeetCode and the create_tree_node function.

    Args:
        root: Root node of the binary tree

    Returns:
        List representation of the binary tree where None represents empty nodes

    Example:
        For a tree:
            4
           / \\
          2   7
         / \\
        1   3
        Returns: [4, 2, 7, 1, 3]
    """
    if not root:
        return []

    result: list[int | None] = []
    queue: list[TreeNode | None] = [root]

    while queue:
        node = queue.pop(0)
        if node:
            result.append(node.val)
            queue.append(node.left)
            queue.append(node.right)
        else:
            result.append(None)

    # Remove trailing None values to match LeetCode format
    while result and result[-1] is None:
        result.pop()

    return result  # type: ignore
