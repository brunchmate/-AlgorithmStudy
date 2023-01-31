n = int(input())
stone = list(map(int,input().split()))
start = 0
end = n-1
mid = (start + end) //2
power = end*(1+abs(stone[0]-stone[end]))

while start <= end:
    power2 = ((end-mid)*(1+abs(stone[mid]-stone[end]))) + ((mid-start)*(1+abs(stone[0]-stone[mid])))

    if power2 < power:
        power = power2
        end-=1
    else:
        start +=1

print(power)

## 이분탐색 카테고리로 분리되어 있어 그렇게 풀려고 했지만 돌의 값들이 정렬되어 있지 않고 문제의 조건들을 생각했을때 정렬을 시켜서도 안된다.
## 이 문제를 풀려면 내가 생각하기에는 각 다리까지 갈 수 있는 값을 저장해 모든 케이스를 확인해야 한다고 생각한다.
''' 
INF = 999999999
n = int(input())
A = list(map(int, input().split()))
# dp[i]는 i까지 가는데 드는 최소 힘
dp = [0] + [INF] * (n - 1)

for i in range(1, n):
    for j in range(0, i):
        power = max((i - j) * (1 + abs(A[i] - A[j])), dp[j]) 
        dp[i] = min(dp[i], power)

print(dp[-1])
'''
