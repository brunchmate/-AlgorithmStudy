# https://school.programmers.co.kr/learn/courses/30/lessons/12977
def solution(nums):
    global answer

    def dfs(cur, total, cnt):
        global answer
        if cnt == 3:
            answer += is_prime(total)
            return
        for i in range(cur, len(nums)):
            if not visited[i]:
                visited[i] = 1
                dfs(i, total + nums[i], cnt + 1)
                visited[i] = 0

    def is_prime(n):
        for i in range(2, int(n ** 0.5) + 1):
            if not n % i:
                return 0
        return 1

    answer = 0
    visited = [0] * len(nums)
    dfs(0, 0, 0)
    return answer
