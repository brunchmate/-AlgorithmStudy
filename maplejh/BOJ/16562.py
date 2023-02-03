# https://www.acmicpc.net/problem/16562
import sys

input = sys.stdin.readline


def union(x, y):
    x = find(x)
    y = find(y)
    if A[x] > A[y]:
        A[x] = A[y]
    elif A[x] < A[y]:
        A[y] = A[x]
    if x < y:
        root[y] = x
    else:
        root[x] = y


def find(x):
    if root[x] != x:
        root[x] = find(root[x])
    return root[x]


N, M, k = map(int, input().split())
A = [0] + list(map(int, input().split()))
root = [i for i in range(N + 1)]

for _ in range(M):
    v, w = map(int, input().split())
    union(v, w)

real = set()
for r in root:
    real.add(find(r))

ans = 0
for i in real:
    ans += A[i]
if ans > k:
    print("Oh no")
else:
    print(ans)

# 29%에서에러남 -> 순서대로 보장 X이므로 같은 집합내에서도 root가 다를수 있다. -> root를 다시 정리하는 과정이 필요하다.
