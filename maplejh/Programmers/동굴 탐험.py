# https://school.programmers.co.kr/learn/courses/30/lessons/67260
from collections import defaultdict, deque

# 위상정렬
# 먼저 방문 해야하는 점이 여러개인 경우
def solution(n, path, order):
    tree = defaultdict(list)
    for px, py in path:
        tree[px].append(py)
        tree[py].append(px)
    indegree = [0] * n
    orders = defaultdict(list)
    for ox, oy in order:
        indegree[oy] += 1
        orders[ox].append(oy)
    if indegree[0]:
        return False
    q = deque()
    q.append(0)
    wait = [0] * n # wait[idx]=1: idx가 나가길 기다리는중
    visited = [0] * n
    visited[0] = 1
    while q:
        x = q.popleft()
        for ox in orders[x]:
            indegree[ox] -= 1
            if wait[ox]:
                q.append(ox)
                visited[ox] = 1
                wait[ox] = 0
        for nx in tree[x]:
            if not visited[nx]:
                if not indegree[nx]:
                    q.append(nx)
                    visited[nx] = 1
                else:
                    wait[nx] = 1  # nx가 아직 조건이 안되서 못나가는 중
    return bool(min(visited))


# 문제조건 잘읽기.... 먼저 방문해야하는 점이 0,1개
from collections import defaultdict, deque


def solution(n, path, order):
    tree = defaultdict(list)
    for px, py in path:
        tree[px].append(py)
        tree[py].append(px)
    orders = [-1] * n
    for ox, oy in order:
        orders[oy] = ox
    if orders[0] != -1:
        return False
    q = deque()
    q.append(0)
    wait = [-1] * n # wait[idx]이 idx가 나가길 기다린다.
    visited = [0] * n
    visited[0] = 1
    while q:
        x = q.popleft()
        if orders[x] != -1 and not visited[orders[x]]:
            wait[orders[x]] = x  # orders[x]가 나가는 걸 기다린다
            continue
        for nx in tree[x]:
            if not visited[nx]:
                q.append(nx)
                visited[nx] = 1
                if wait[nx] != -1:
                    q.append(wait[nx])
    return bool(min(visited))
