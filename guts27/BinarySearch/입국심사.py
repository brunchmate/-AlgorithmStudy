n,m = map(int,input().split())
immigration= []
for _ in range(n):
    immigration.append(int(input()))
immigration.sort()
start = 0
result=0
end = immigration[0]*m
while start <= end:
    mid = (start+end) // 2
    num = 0
    for im in immigration:
        num += mid //im

    if num >= m:
        end = mid - 1
        result = mid
    else:
        start = mid + 1

print(result)
