# https://www.acmicpc.net/problem/22871
import sys
from collections import deque

input = sys.stdin.readline


def bfs(flag):
    q = deque()
    visited = [0] * N
    q.append(0)  # k, x
    visited[0] = 0
    while q:
        x = q.popleft()
        if x == N - 1:
            return True
        for nx in range(x + 1, N):
            if visited[nx]:
                continue
            power = (nx - x) * (1 + abs(A[x] - A[nx]))
            if power <= flag:
                q.append(nx)
                visited[nx] = 1
    return False


N = int(input())
A = list(map(int, input().split()))
start = 0
end = 5000000000
ans = end
while start <= end:
    mid = (start + end) // 2
    if bfs(mid):
        end = mid - 1
        ans = mid
    else:
        start = mid + 1
print(ans)

# 처음에 dp로 통과
# dp = [5000000000] * N  # idx까지 오는데 최소비용
# dp[0] = 0
# for i in range(1, N):
#     tmp = []  # k 번째 돌을 거쳐서 i로 가는데 필요한 힘
#     for k in range(i):
#         tmp.append(max(dp[k], (i - k) * (1 + abs(A[i] - A[k])))) # 시간 초과를 줄이는 방법 (매번 비교하지 X)
#     dp[i] = min(tmp)
# print(dp[-1])
