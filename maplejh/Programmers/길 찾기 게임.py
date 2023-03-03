# https://school.programmers.co.kr/learn/courses/30/lessons/42892
import sys

sys.setrecursionlimit(10 ** 6)


class Node:
    def __init__(self, idx, x):
        self.val = idx
        self.x = x
        self.left = None
        self.right = None


class Tree:
    def __init__(self, root, x):
        self.root = Node(root, x)

    def insert(self, idx, x):
        cur_node = self.root
        while True:
            if cur_node.x > x:
                if cur_node.left == None:
                    cur_node.left = Node(idx, x)
                    break
                else:
                    cur_node = cur_node.left
            else:
                if cur_node.right == None:
                    cur_node.right = Node(idx, x)
                    break
                else:
                    cur_node = cur_node.right

    def pre_order(self):
        res = []

        def order(parent):
            res.append(parent.val)
            if parent.left:
                order(parent.left)
            if parent.right:
                order(parent.right)

        order(self.root)
        return res

    def post_order(self):
        res = []

        def order(parent):
            if parent.left:
                order(parent.left)
            if parent.right:
                order(parent.right)
            res.append(parent.val)

        order(self.root)
        return res


def solution(nodeinfo):
    answer = []
    nodes = []
    for idx, node in enumerate(nodeinfo):
        nodes.append((node[0], node[1], idx + 1))
    nodes.sort(key=lambda x: (-x[1], x[0]))
    tree = Tree(nodes[0][2], nodes[0][0])
    for i in range(1, len(nodes)):
        tree.insert(nodes[i][2], nodes[i][0])
    answer.append(tree.pre_order())
    answer.append(tree.post_order())

    return answer
