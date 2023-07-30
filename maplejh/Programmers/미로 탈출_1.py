from collections import defaultdict
import heapq


def solution(n, start, end, roads, traps):
    answer = 0
    trap = defaultdict(int)
    for ti, t in enumerate(traps):
        trap[t] = ti + 1
    board = defaultdict(list)
    for p, q, s in sorted(roads):
        board[p].append((q, s, 0))
        if trap[p] or trap[q]:
            board[q].append((p, s, 1))
    dist = [[1e9] * (2 ** trap[traps[-1]] + 1) for _ in range(n + 1)]
    print(trap[traps[-1]])
    q = [(0, start, 0)]
    while q:
        cnt, x, state = heapq.heappop(q)
        if dist[x][state] < cnt:
            continue
        cur = 0
        if trap[x]:
            cur = (state & (1 << trap[x])) >> trap[x]
        for nx, nc, nd in board[x]:
            if trap[nx]:
                if cur ^ ((state & (1 << trap[nx])) >> trap[nx]) == nd:
                    new_state = state ^ (1 << trap[nx])
                    print(new_state)
                    if dist[nx][new_state] > cnt + nc:
                        dist[nx][new_state] = cnt + nc
                        heapq.heappush(q, (cnt + nc, nx, new_state))
            else:
                if nd == cur:
                    if dist[nx][state] > cnt + nc:
                        dist[nx][state] = cnt + nc
                        heapq.heappush(q, (cnt + nc, nx, state))
    return min(dist[end])

solution(3, 1, 3, [[1, 2, 2], [3, 2, 3]], [2])
solution(4, 1, 4, [[1, 2, 1], [3, 2, 1], [2, 4, 1]], [2, 3])