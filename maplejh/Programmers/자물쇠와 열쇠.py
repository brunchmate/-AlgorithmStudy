# https://school.programmers.co.kr/learn/courses/30/lessons/60059
def solution(key, lock):
    def check(arr):
        for r in range(n):
            for c in range(n):
                if board[r + i][c + j] == arr[r][c]:
                    return False
        return True

    m = len(key)
    n = len(lock)
    mn = m + 2 * (n - 1)
    board = [[0] * mn for _ in range(mn)]
    for i in range(m):
        for j in range(m):
            board[i + n - 1][j + n - 1] = key[i][j]
    for i in range(mn - n):
        for j in range(mn - n):
            for _ in range(4):
                lock = list(zip(*lock))[::-1]
                if check(lock):
                    return True
    return False
