# https://school.programmers.co.kr/learn/courses/30/lessons/72416
from collections import defaultdict


def solution(sales, links):
    def dfs(x):
        dp[x][1] = sales[x]
        if not board[x]:
            return
        flag = 1e9
        for nx in board[x]:
            dfs(nx)
            dp[x][1] += min(dp[nx])
            dp[x][0] += min(dp[nx])
            flag = min(dp[nx][1] - dp[nx][0], flag)
        dp[x][0] += max(flag, 0)  # flag가 음수가 나오면 dp[][1]인 경우가 적어도 한번 있다는 뜻

    n = len(sales)
    dp = [[0, 0] for _ in range(n)]
    board = defaultdict(list)
    for a, b in links:
        board[a - 1].append(b - 1)
    dfs(0)
    return min(dp[0])
