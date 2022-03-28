import sys

sys.setrecursionlimit(2000)


class Node:
    def __init__(self, id, x, y):
        self.id = id
        self.x = x
        self.y = y
        self.left = None
        self.right = None

    # 오름차순
    def __lt__(self, other):
        if self.y == other.y:
            return self.x < other.x
        return self.y > other.y


def addNode(parent, child):
    if child.x < parent.x:
        if parent.left is None:
            parent.left = child
        else:
            addNode(parent.left, child)
    else:
        if parent.right is None:
            parent.right = child
        else:
            addNode(parent.right, child)


def preorder(answer, node):
    if node is None:
        return
    answer.append(node.id)
    preorder(answer, node.left)
    preorder(answer, node.right)


def postorder(answer, node):
    if node is None:
        return
    postorder(answer, node.left)
    postorder(answer, node.right)
    answer.append(node.id)


def solution(nodeinfo):
    node_list = []
    for i in range(len(nodeinfo)):
        node_list.append(Node(i + 1, nodeinfo[i][0], nodeinfo[i][1]))

    node_list.sort()
    root = node_list[0]
    for i in range(1, len(nodeinfo)):
        addNode(root, node_list[i])
    preorder_list = []
    postorder_list = []
    preorder(preorder_list, root)
    postorder(postorder_list, root)

    return [preorder_list, postorder_list]


print(solution([[5, 3], [11, 5], [13, 3], [3, 5], [6, 1], [1, 3], [8, 6], [7, 2], [2, 2]]))
