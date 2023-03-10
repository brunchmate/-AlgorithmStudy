# https://school.programmers.co.kr/learn/courses/30/lessons/60061
def solution(n, build_frame):
    def build(x, y, a):
        if a:  # 보
            # 한쪽 끝 부분이 기둥 위에 있거나
            if board[x - 1][y][0] or (y < n and board[x - 1][y + 1][0]):
                return True
            # 양쪽 끝 부분이 다른 보와 동시에 연결
            elif 0 < y < n and board[x][y - 1][1] and board[x][y + 1][1]:
                return True
        else:  # 기둥
            # 바닥에 있거나
            if x == 0:
                return True
            # 보의 한쪽 끝 부분 위에 있거나
            elif board[x][y][1] or (y > 0 and board[x][y - 1][1]):
                return True
            # 다른 기둥 위에
            elif board[x - 1][y][0]:
                return True
        return False

    board = [[[0, 0] for _ in range(n + 1)] for _ in range(n + 1)]
    for by, bx, aa, bb in build_frame:
        if bb:  # 설치
            if build(bx, by, aa):
                board[bx][by][aa] = 1
        else:  # 삭제
            board[bx][by][aa] = 0
            for dx, dy, da in [[0, 0, 0], [0, 0, 1], [0, -1, 1], [0, 1, 0], [0, 1, 1], [1, 0, 0], [1, 0, 1],
                               [1, -1, 1]]:
                nx = bx + dx
                ny = by + dy
                if -1 < nx < n + 1 and -1 < ny < n + 1:
                    if board[nx][ny][da] and not build(nx, ny, da):
                        board[bx][by][aa] = 1
                        break
    answer = []
    for j in range(n + 1):
        for i in range(n + 1):
            for k in range(2):
                if board[i][j][k]:
                    answer.append([j, i, k])
    if not answer:
        answer.append([])
    return answer
