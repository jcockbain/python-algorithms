from tree import TreeNode


def inorder_traversal(root, res=None):
    if root is None:
        return []
    if res is None:
        res = []
    inorder_traversal(root.left, res)
    res.append(root.val)
    inorder_traversal(root.right, res)
    return res


def inorder_traversal_iterative(root, res=None):
    res, stack = [], []
    current = root
    while current or len(stack) > 0:
        while current:
            stack.append(current)
            current = current.left
        current = stack.pop()
        res.append(current.val)
        current = current.right
    return res
