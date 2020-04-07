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
