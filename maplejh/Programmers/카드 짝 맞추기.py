# https://school.programmers.co.kr/learn/courses/30/lessons/72415
from collections import defaultdict
import heapq


def solution(board, r, c):
    def move(sx, sy, ex, ey):
        q = [(0, sx, sy)]
        while q:
            cnt, x, y = heapq.heappop(q)
            if x == ex and y == ey:
                board[ex][ey] = 0
                return cnt
            for dx, dy in d:
                nx = x
                ny = y
                for k in range(4):
                    nx += dx
                    ny += dy
                    if -1 < nx < 4 and -1 < ny < 4:
                        if board[nx][ny]:  # 만나는 첫번째 카드
                            heapq.heappush(q, (cnt + 1, nx, ny))
                            break
                        if k == 0:  # 한 칸 이동
                            heapq.heappush(q, (cnt + 1, nx, ny))
                    else:  # 마지막 칸
                        if k > 1:
                            nx -= dx
                            ny -= dy
                            heapq.heappush(q, (cnt + 1, nx, ny))
                        break

    def game(x, y, cnt):
        global answer
        if cnt >= answer:
            return
        if not visited:
            answer = cnt
            return
        for ck in card.keys():
            if ck not in visited:
                continue
            visited.remove(ck)
            for k in range(2):
                game(*card[ck][k],
                     move(x, y, *card[ck][abs(k - 1)]) + move(*card[ck][abs(k - 1)], *card[ck][k]) + cnt + 2)
                board[card[ck][0][0]][card[ck][0][1]] = ck
                board[card[ck][1][0]][card[ck][1][1]] = ck
            visited.add(ck)

    d = [(-1, 0), (1, 0), (0, 1), (0, -1)]
    global answer
    answer = 10e9
    card = defaultdict(list)
    visited = set()
    for i in range(4):
        for j in range(4):
            if board[i][j]:
                card[board[i][j]].append((i, j))
                visited.add(board[i][j])
    game(r, c, 0)
    return answer
