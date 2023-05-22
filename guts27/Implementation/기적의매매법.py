n = int(input())
jun = [n,0]
sung = [n,0]
arr = list(map(int,input().split()))
down = 0
up = 0
if arr[0] <= n:
    jun[0],jun[1] = (n % arr[0]),(n // arr[0])

for i in range(1,13):
    if arr[i] <= jun[0]:
        jun[1] = jun[1]+(jun[0] // arr[i])
        jun[0] = (jun[0] % arr[i])
        
    if arr[i-1] < arr[i]:
        up += 1
        down = 0
    elif arr[i-1] > arr[i]:
        down += 1
        up = 0
    else:
        down = 0
        up = 0
    if down == 3:
        sung[1] = sung[1]+(sung[0] // arr[i])
        sung[0] = (sung[0] % arr[i])
    elif up == 3:
        sung[0] = sung[0] + arr[i]*sung[1]
        sung[1] = 0
        
result_j = jun[0] + jun[1]*arr[13]
result_s = sung[0] + sung[1]*arr[13]
if result_j > result_s:
    print("BNP")
elif result_j < result_s:
    print("TIMING")
else:
    print("SAMESAME")
        