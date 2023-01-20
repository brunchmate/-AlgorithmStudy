# https://www.acmicpc.net/problem/22946
import sys
from collections import defaultdict, deque

input = sys.stdin.readline


def dfs(x, depth):
    if x not in contain.keys():
        cnt[k] = max(cnt[k], depth)
        return
    for nx in contain[x]:
        dfs(nx, depth + 1)


def bfs(sx):
    q = deque()
    q.append((1, sx))
    while q:
        c, x = q.popleft()
        if x not in contain.keys():
            continue
        for nx in contain[x]:
            q.append((c + 1, nx))
    cnt[k] = c


N = int(input())
eq = dict()
rev_contain = [0] * (N + 1)  # 자신을 포함하고 있는 원 중에서 가장 작은 원
contain = defaultdict(list)
for i in range(1, N + 1):
    x1, y1, r1 = map(int, input().split())
    eq[i] = [x1, y1, r1]
    for j in range(1, i):
        x2, y2, r2 = eq[j]
        # 원이 내부에 있는지 확인
        d = ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0.5
        if abs(r1 - r2) >= d:
            if r1 > r2:
                big = i
                small = j
            elif r1 < r2:
                big = j
                small = i
            if not rev_contain[small]:
                rev_contain[small] = big
            else:
                if eq[big][-1] < eq[rev_contain[small]][-1]:
                    rev_contain[small] = big
for i in range(1, N + 1):
    contain[rev_contain[i]].append(i)
answer = 0
cnt = [1] * (N + 1)
for k in contain.keys():
    # dfs(k, 1)
    bfs(k)
for k, v in contain.items():
    res = []
    for vv in v:
        res.append(cnt[vv])
    answer = max(answer, sum(sorted(res, reverse=True)[:2]))
print(answer)
