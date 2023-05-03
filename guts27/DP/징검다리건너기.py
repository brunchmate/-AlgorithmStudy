n,m = map(int,input().split())
stones = list(map(int,input().split()))
dp = [0 for _ in range(n)]
dp[0] = 1

for i in range(n):
    if dp[i] == 0:
        continue
    for j in range(i+1,n):
        power = (j-i)*(1+abs(stones[i]-stones[j]))
        if power <= m:
            dp[j] = 1
    if dp[n-1] == 1:
        print("YES")
        exit()
print("NO")
