# https://school.programmers.co.kr/learn/courses/30/lessons/17679
def solution(m, n, board):
    answer = 0
    board = list(map(list, board))

    def game():
        res = set()
        for i in range(m - 1):
            for j in range(n - 1):
                if board[i][j]:
                    if board[i][j] == board[i][j + 1] == board[i + 1][j] == board[i + 1][j + 1]:
                        res.add((i, j))
                        res.add((i, j + 1))
                        res.add((i + 1, j))
                        res.add((i + 1, j + 1))
        for i, j in res:
            board[i][j] = ""
        for j in range(n):
            ground = m
            for i in range(m - 1, -1, -1):
                if board[i][j]:
                    tmp = board[i][j]
                    board[i][j] = ""
                    board[ground - 1][j] = tmp
                    ground -= 1
        return len(res)

    while True:
        flag = game()
        if not flag:
            break
        answer += flag
    return answer
