# https://school.programmers.co.kr/learn/courses/30/lessons/64061
def solution(board, moves):
    answer = 0
    j = 0
    stack = []
    n = len(board)
    for m in moves:
        j = m - 1
        for i in range(n):
            if not board[i][j]:
                continue
            else:
                if stack and stack[-1] == board[i][j]:
                    stack.pop()
                    answer += 2
                else:
                    stack.append(board[i][j])
                board[i][j] = 0
                break
    return answer
