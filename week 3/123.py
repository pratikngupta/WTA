class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def build_tree():
    root = TreeNode(1)
    root.left = TreeNode(7)
    root.left.left = TreeNode(2)
    root.left.right = TreeNode(6)
    root.left.right.left = TreeNode(12)
    root.left.right.right = TreeNode(11)
    root.right = TreeNode(9)
    root.right.right = TreeNode(13)
    root.right.right.left = TreeNode(5)

    return root


# find the node with k distance from target

def find_node_disrance_k(root, target, k):
    result = []
    list = postorder_traversal(root)

    for node in list:
        g = lca(root, target, node)
        distance = dfs(g, target) + dfs(g, node)
        if distance == k:
            result.append(node)

    return result


# find distance between 2 node
def lca(root, p, q):
    if root is None or root.val in [p, q]:
        return root
    left = lca(root.left, p, q)
    right = lca(root.right, p, q)
    if left is None:
        return right
    if right is None:
        return left
    return root


def dfs(root, v):
    if root is None:
        return -1
    if root.val == v:
        return 0
    left, right = dfs(root.left, v), dfs(root.right, v)
    if left == right == -1:
        return -1
    return 1 + max(left, right)


def postorder_traversal(root):
    res = []
    if root:
        res = postorder_traversal(root.left)
        res = res + postorder_traversal(root.right)
        res.append(root.val)
    return res


if __name__ == "__main__":
    root = build_tree()
    target = 1
    k = 3

    print(find_node_disrance_k(root, target, k))

