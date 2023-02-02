# https://www.acmicpc.net/problem/4358
import sys

input = sys.stdin.readline


def search(tree, depth):
    for key in sorted(tree.keys()):
        if key == '\n':
            print(f'{depth} {(tree[key] / cnt) * 100:.4f}')
        else:
            search(tree[key], depth + key)


root = {}
cnt = 0
while True:
    ss = input().rstrip()
    if not ss:
        break
    node = root
    for s in ss:
        if s not in node:
            node[s] = {}
        node = node[s]
    if "\n" in node:
        node["\n"] += 1
    else:
        node["\n"] = 1
    cnt += 1

search(root, '')

# 클래스로도 트라이자료구조 만들어보기..
