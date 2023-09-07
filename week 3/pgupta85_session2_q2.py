"""
    Nane: Pratik Narendra Gupta
    Program: Software Engineering - 3rd year
"""


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

def find_node_distance_k(root, target, k):
    result = []

    def dfs(node, distance):
        if not node:
            return
        if distance == k:
            result.append(node.val)
        dfs(node.left, distance + 1)
        dfs(node.right, distance + 1)

    def find_target(node):
        if not node:
            return -1
        if node.val == target:
            dfs(node, 0)
            return 1
        left_distance = find_target(node.left)
        right_distance = find_target(node.right)
        if left_distance != -1:
            if left_distance == k:
                result.append(node.val)
            dfs(node.right, left_distance + 1)
            return left_distance + 1
        if right_distance != -1:
            if right_distance == k:
                result.append(node.val)
            dfs(node.left, right_distance + 1)
            return right_distance + 1
        return -1

    find_target(root)
    return result

if __name__ == "__main__":
    root = build_tree()

    print("All case use same Tree provided in the question")

    print()

    print("Case 1: Given in the question")
    print(("Target = 9, K = 2"))
    print("Output: ", find_node_distance_k(root, 9, 2))

    print()

    print("Case 2")
    print(("Target = 5, K = 6"))
    print("Output: ", find_node_distance_k(root, 5, 6))

    print()

    print("Case 3")
    print(("Target = 1, K = 4"))
    print("Output: ", find_node_distance_k(root, 1, 4))

    print()
    print("Case 4")
    print(("Target = 1, K = 3"))
    print("Output: ", find_node_distance_k(root, 1, 3))