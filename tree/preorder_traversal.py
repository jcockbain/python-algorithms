from tree import TreeNode


def preorder_traversal(root, res=None):
    if root is None:
        return []
    if res is None:
        res = []
    res.append(root.val)
    preorder_traversal(root.left, res)
    preorder_traversal(root.right, res)
    return res


def preorder_traversal_iterative(root, res=None):
    if not root:
        return []

    stack, output = [root, ], []
    while stack:
        root = stack.pop()
        if root is not None:
            output.append(root.val)
            if root.right is not None:
                stack.append(root.right)
            if root.left is not None:
                stack.append(root.left)
    return output
