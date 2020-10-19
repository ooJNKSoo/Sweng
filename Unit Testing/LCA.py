class Node:

    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def lca(root, num0, num1):
    while root:
        if root.data > num0 and root.data > num1:
            root = root.left

        elif root.data < num0 and root.data < num1:
            root = root.right

        else:
            break

    return root