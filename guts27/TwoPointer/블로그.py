n,x = map(int,input().split())
visited = list(map(int,input().split()))
 
if max(visited) == 0:
    print('SAD')
else:
    sumnum = sum(visited[:x])
    maxnum = sumnum
    cnt = 1
 
    for i in range(x,n):
        sumnum += visited[i]
        sumnum -= visited[i-x]
        if sumnum > maxnum:
            maxnum = sumnum
            cnt = 1
        elif sumnum == maxnum:
            cnt += 1
 
    print(maxnum)
    print(cnt)    
    
    ## 슬라이딩 윈도우로 풀어야한다.
