n = int(input())
drinks = list(map(int,input().split()))
max_num = max(drinks)
drinks.remove(max_num)
print(sum(drinks)/2 + max_num)

drinks.sort()

total = drinks[-1]
for i in range(N-1):
    total += drinks[i]/2
