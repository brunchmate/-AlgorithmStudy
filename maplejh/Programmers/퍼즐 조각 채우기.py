# https://school.programmers.co.kr/learn/courses/30/lessons/84021
from collections import defaultdict, deque


def solution(game_board, table):
    def rotate90(loc, r, c):
        tmp = [[0] * c for _ in range(r)]
        for lx, ly in loc:
            tmp[lx][ly] = 1
        tmp = list(zip(*tmp))[::-1]
        res = []
        for x in range(c):
            for y in range(r):
                if tmp[x][y]:
                    res.append([x, y])
        trans_res = list(zip(*res))
        min_x = min(trans_res[0])
        min_y = min(trans_res[1])
        for idx in range(len(res)):
            res[idx][0] -= min_x
            res[idx][1] -= min_y
        return sorted(res)

    def bfs(sx, sy, board, flag):
        nonflag = abs(flag - 1)
        q = deque([(sx, sy)])
        board[sx][sy] = nonflag
        res = [[sx, sy]]
        while q:
            x, y = q.popleft()
            for dx, dy in d:
                nx = x + dx
                ny = y + dy
                if -1 < nx < n and -1 < ny < n:
                    if board[nx][ny] == flag:
                        board[nx][ny] = nonflag
                        q.append((nx, ny))
                        res.append([nx, ny])
        trans_res = list(zip(*res))
        min_x = min(trans_res[0])
        min_y = min(trans_res[1])
        max_x = max(trans_res[0])
        max_y = max(trans_res[1])
        for idx in range(len(res)):
            res[idx][0] -= min_x
            res[idx][1] -= min_y
        return sorted(res), max_x, max_y

    def match(wl, wz):
        for pi, pzs in enumerate(piece[wl]):
            if (wl, pi) in visited:
                continue
            for pz in pzs:
                if pz == wz:
                    visited.add((wl, pi))
                    return
        return

    d = [(-1, 0), (0, 1), (1, 0), (0, -1)]
    n = len(game_board)
    piece = defaultdict(list)
    for i in range(n):
        for j in range(n):
            if table[i][j]:
                pz, row, col = bfs(i, j, table, 1)
                puzzles = [pz]
                for _ in range(3):
                    pz = rotate90(pz, row + 1, col + 1)
                    row, col = col, row
                    puzzles.append(pz)
                piece[len(pz)].append(puzzles)
    visited = set()
    for i in range(n):
        for j in range(n):
            if not game_board[i][j]:
                blank, _, _ = bfs(i, j, game_board, 0)
                match(len(blank), blank)
    answer = 0
    for vx, _ in visited:
        answer += vx
    return answer
