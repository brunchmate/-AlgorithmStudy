from collections import defaultdict, deque


def solution(info, edges):
    answer = 0
    board = defaultdict(list)
    for a, b in edges:
        board[a].append(b)
        board[b].append(a)
    visited = [[0] * 2 ** len(info) for _ in range(len(info))]
    q = deque([(1, 0, 0, 1)])  # 양, 늑대, 현재위치, 방문상태
    visited[0][1] = 1
    while q:
        sheep, wolf, x, state = q.popleft()
        if answer < sheep:
            answer = sheep
        for nx in board[x]:
            cur = (state & (1 << nx)) >> nx  # 예전에 방문한 점인지
            new_state = state | (1 << nx)
            if not visited[nx][new_state]:
                new_sheep = sheep
                new_wolf = wolf
                if not cur:
                    if info[nx] == 1:
                        new_wolf += 1
                    else:
                        new_sheep += 1
                if new_sheep > new_wolf:
                    q.append((new_sheep, new_wolf, nx, new_state))
                    visited[nx][new_state] = 1
    return answer
