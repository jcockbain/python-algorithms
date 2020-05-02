from collections import deque


def levelorder_traversal(root):
    levels = []

    if not root:
        return levels

    def helper(node, level):
        if len(levels) == level:
            levels.append([])

        levels[level].append(node.val)

        if node.left:
            helper(node.left, level + 1)
        if node.right:
            helper(node.right, level + 1)

    helper(root, 0)
    return levels


def levelorder_traversal_iterative(root):
    levels = []
    if not root:
        return levels
    level = 0
    queue = deque([root, ])
    while queue:
        levels.append([])
        for _ in range(len(queue)):
            node = queue.popleft()
            levels[level].append(node.val)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        level += 1
    return levels
