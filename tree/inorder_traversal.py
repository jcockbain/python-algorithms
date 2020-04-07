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
