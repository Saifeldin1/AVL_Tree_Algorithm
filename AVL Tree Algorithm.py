class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
        self.height = 0


def get_height(node):
    if node is None:
        return -1
    return node.height


def get_balance_factor(node):
    if node is None:
        return 0
    return get_height(node.left) - get_height(node.right)


def LL_rotation(root):
    new_root = root.left
    root.left = new_root.right
    new_root.right = root

    root.height = 1 + max(get_height(root.left), get_height(root.right))
    new_root.height = 1 + max(get_height(new_root.left), get_height(new_root.right))

    return new_root


def RR_rotation(root):
    new_root = root.right
    root.right = new_root.left
    new_root.left = root


    root.height = 1 + max(get_height(root.left), get_height(root.right))
    new_root.height = 1 + max(get_height(new_root.left), get_height(new_root.right))

    return new_root


def insert(node, val):
    if node is None:
        node = Node(val)
        return node

    if val < node.data:
        node.left = insert(node.left, val)
    elif val > node.data:
        node.right = insert(node.right, val)
    else:
        return node 

    node.height = 1 + max(get_height(node.left), get_height(node.right))

    balance = get_balance_factor(node)

    if balance > 1:
        if val < node.left.data:
            return LL_rotation(node)
        else:
            node.left = RR_rotation(node.left)
            return LL_rotation(node)
    elif balance < -1:
        if val > node.right.data:
            return RR_rotation(node)
        else:
            node.right = LL_rotation(node.right)
            return RR_rotation(node)

    return node


def print_tree(root, level=0, prefix="Root: "):
    if root is not None:
        print(" " * (level * 4) + prefix + str(root.data))
        if root.left is not None or root.right is not None:
            print_tree(root.left, level + 1, "L--- ")
            print_tree(root.right, level + 1, "R--- ")


root = None
root = insert(root, 10)
root = insert(root, 20)
root = insert(root, 5)
root = insert(root, 30)
root = insert(root, 15)
root = insert(root, 31)
root = insert (root, 32)


print_tree(root)
