# https://school.programmers.co.kr/learn/courses/30/lessons/12971
def solution(sticker):
    answer = 0
    n = len(sticker)
    if n == 1:
        return sticker[0]
    # 첫번째 스티커 O
    dp = [0] * n
    dp[0] = sticker[0]
    dp[1] = sticker[0]
    for i in range(2, n - 1):
        dp[i] = max(dp[i - 2] + sticker[i], dp[i - 1])
    answer = dp[-2]
    # 첫번째 스티커 X
    dp[0] = 0
    dp[1] = sticker[1]
    for i in range(2, n):
        dp[i] = max(dp[i - 2] + sticker[i], dp[i - 1])
    answer = max(answer, dp[-1])
    return answer
