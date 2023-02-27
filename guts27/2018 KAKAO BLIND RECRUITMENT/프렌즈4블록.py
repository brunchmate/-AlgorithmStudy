def solution(m, n, board):
    answer = 0
    for i in range(m):
        board[i] = list(board[i])
    print(board)
    while True:
        remove = []
    # 지워야 할 것들 다 담고
        for i in range(m-1):
            for j in range(n-1):
                if board[i][j] == '':
                    continue
                if board[i][j] == board[i][j+1] ==board[i+1][j] ==board[i+1][j+1]:
                    remove.append((i,j))
                    remove.append((i,j+1))
                    remove.append((i+1,j))
                    remove.append((i+1,j+1))
        # set()한값 다시 담아주기
        remove = set(remove)
                
        # 지우기
        if len(remove) == 0:
            break
        else:
            answer += len(remove)
            for i,j in remove:
                board[i][j] = ''
        #지운만큼 내리기
        for j in range(n):
            for i in range(m):
                if board[i][j] == '':
                    for x in range(i, 0, -1):
                        board[x][j] = board[x-1][j]
                        board[x-1][j] = ''
                    
    return answer
solution(4,5,["CCBDE", "AAADE", "AAABF", "CCBBF"])