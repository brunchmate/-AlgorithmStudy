# https://school.programmers.co.kr/learn/courses/30/lessons/42894
from collections import deque, defaultdict


def solution(board):
    def game(sx, sy):
        q = deque()
        visited[sx][sy] = 1
        q.append((sx, sy))
        loc = set()
        loc.add((sx, sy))
        while q:
            x, y = q.popleft()
            for di in range(3):
                nx = d[di][0] + x
                ny = d[di][1] + y
                if -1 < nx < n and -1 < ny < n:
                    if visited[nx][ny]:
                        continue
                    if board[nx][ny] == board[sx][sy]:
                        visited[nx][ny] = 1
                        q.append((nx, ny))
                        loc.add((nx, ny))
        # 가능한 블록인지 확인 -> x-1 보다 x에 에있는 블록수가 적으면 안됨
        cnt = defaultdict(int)
        for lx, ly in loc:
            cnt[lx] += 1
        prior = -1
        for k in sorted(cnt.keys()):
            if cnt[prior] > cnt[k]:
                break
            prior = k
        else:
            answer[board[sx][sy]] = loc
            return True
        # 불가능한 경우 마킹
        for lx, ly in loc:
            if ly in block.keys():
                block[ly] = min(block[ly], lx)
            else:
                block[ly] = lx
        return False

    d = [(0, 1), (0, -1), (1, 0)]
    answer = dict()
    n = len(board)
    visited = [[0] * n for _ in range(n)]
    block = dict()
    for i in range(n):
        for j in range(n):
            if board[i][j] and not visited[i][j]:
                game(i, j)
    # 위에서 막아서 못 내려 오는 경우 -> 안되는 블록들이 새로 생겨남 - 안 생길 때까지 반복
    while True:
        new_block = set()
        for by in block.keys():
            color = defaultdict(int)
            for bx in range(block[by], n):
                color[board[bx][by]] += 1
            for ck, cv in color.items():
                if cv == 1 and ck in answer.keys():
                    new_block.add(ck)
        if not new_block:
            break
        block = dict()
        # 불가능한 경우 마킹
        for nb in new_block:
            for ax, ay in answer[nb]:
                if ay in block.keys():
                    block[ay] = min(block[ay], ax)
                else:
                    block[ay] = ax
            del answer[nb]
    return len(answer)

'''
1. 주어진 블록 모양 중에 직사각형으로 만들 수 있는 블록 count
2. 1번 중에 위에서 막아서 못하는 답 빼기
3. 2에서 새로 생긴 막는 블록들에 영향을 받는 답 빼기 (2가 안 생길 때까지 2반복)
'''