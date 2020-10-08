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


root = Node(20)
root.left = Node(8)
root.right = Node(22)
root.left.left = Node(4)
root.left.right = Node(12)
root.left.right.left = Node(10)
root.left.right.right = Node(14)

num0 = 10
num1 = 14
t = lca(root, num0, num1)
print("LCA of %d and %d is %d" % (num0, num1, t.data))

num0 = 14
num1 = 8
t = lca(root, num0, num1)
print("LCA of %d and %d is %d" % (num0, num1, t.data))

num0 = 10
num1 = 22
t = lca(root, num0, num1)
print("LCA of %d and %d is %d" % (num0, num1, t.data))