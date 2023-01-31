import sys
INF = sys.maxsize

n = int(input())
data = list(map(int,input().split()))
data.sort()

minnum = INF
result= []
start = 0
end = n-1

while start < end:
    num = data[start]+data[end]
    if abs(num) < minnum:
        minnum = abs(num)
        result = (data[start], data[end])

    if num < 0:
        start+= 1
    else:
        end -= 1

print(*result)
