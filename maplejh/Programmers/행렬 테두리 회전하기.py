# https://school.programmers.co.kr/learn/courses/30/lessons/77485
def solution(rows, columns, queries):
    def rotate(a, b, c, d):
        prior = board[a][b]
        res = prior
        for y in range(b + 1, d):
            tmp = board[a][y]
            board[a][y] = prior
            prior = tmp
            if res > prior:
                res = prior
        for x in range(a, c):
            tmp = board[x][d]
            board[x][d] = prior
            prior = tmp
            if res > prior:
                res = prior
        for y in range(d, b, -1):
            tmp = board[c][y]
            board[c][y] = prior
            prior = tmp
            if res > prior:
                res = prior
        for x in range(c, a - 1, -1):
            tmp = board[x][b]
            board[x][b] = prior
            prior = tmp
            if res > prior:
                res = prior
        return res

    answer = []
    board = [[i * columns + j + 1 for j in range(columns)] for i in range(rows)]
    for q in queries:
        answer.append(rotate(*map(lambda x: x - 1, q)))
    return answer
