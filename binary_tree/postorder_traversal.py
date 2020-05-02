from tree import TreeNode


def postorder_traversal(root, res=None):
    if root is None:
        return []
    if res is None:
        res = []
    postorder_traversal(root.left, res)
    postorder_traversal(root.right, res)
    res.append(root.val)
    return res


def postorder_traversal_iterative(root):
    if root is None:
        return
    stack, output = [root, ], []
    while stack:
        root = stack.pop()
        output.append(root.val)
        if root.left is not None:
            stack.append(root.left)
        if root.right is not None:
            stack.append(root.right)
    return output[::-1]
