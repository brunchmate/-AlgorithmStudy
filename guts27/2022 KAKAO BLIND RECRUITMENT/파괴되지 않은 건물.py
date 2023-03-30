def solution(board, skill):
    answer = 0
    n = len(board)
    m = len(board[0])
    arr = [[0 for _ in range(m)] for _ in range(n)]
    
    for t, r1, c1, r2, c2, d in skill:
        if t == 1:
            arr[r1][c1] -= d
            if r2+1 < n and c2+1 <m:
                arr[r2+1][c2+1] -= d
            if c2+1 < m:
                arr[r1][c2+1] += d
            if r2+1<n:
                arr[r2+1][c1] += d
        else:
            arr[r1][c1] += d
            if r2+1 < n and c2+1 <m:
                arr[r2+1][c2+1] += d
            if c2+1 < m:
                arr[r1][c2+1] -= d
            if r2+1<n:
                arr[r2+1][c1] -= d
    
    for j in range(m):
        for i in range(n-1):
            arr[i+1][j] += arr[i][j]
            
    for i in range(n):
        for j in range(m-1):
            arr[i][j+1] += arr[i][j]
            
    for i in range(n):
        for j in range(m):
            if arr[i][j] + board[i][j] > 0:
                answer += 1
    return answer
