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
