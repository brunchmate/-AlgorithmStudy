#n = int(input())
n = 3
student = [False]*((n**n)+1)
graph = [[2 for _ in range(n)] for _ in range(n)]
for x in range(n):
    for y in range(n):
        if (x == 0 and y == 0) or (x == 0 and y == n-1) or (x == n-1 and y == 0)or (x == n-1 and y == n-1):
            continue
        if x == 0 or y == 0 or x == n-1 or y == n-1:
            graph[x][y] += 1
        else:
            graph[x][y] += 2
dx = [-1,0,1,0]
dy = [0,1,0,-1]
result2 = []
result1 = {}

arrlist = [[4, 2, 5, 1, 7], [3, 1, 9, 4, 5], [9, 8, 1, 2, 3], [8, 1, 9, 3, 4], [7, 2, 3, 4, 8], [1, 9, 2, 5, 7], [6, 5, 2, 3, 4], [5, 1, 9, 2, 8], [2, 9, 3, 1, 4]]
#for _ in range(n**n):
    #arr = list(map(int,input().split()))
for arr in arrlist:   
    result1 = {}
    for i in range(1,5):
        if student[arr[i]] != False:
            x,y = student[arr[i]][0],student[arr[i]][1]
            for y in range(4):
                nx,ny = x+dx[i],y+dy[i]
                if 0<=nx<n and 0<=y<n and graph[nx][ny]!= True:
                    if (nx,ny) in result1:
                        result1[(nx,ny)] += 1
                    else:
                        result1[(nx,ny)] = 1
        
        if len(result1) == 1:
            x,y = result1.value()
            graph[x][y] == True
            student[arr[0]] = [x,y]
            continue
        elif len(result1) == 0:
            #제일 큰값
            max_num = 0
            max_graph = []
            for x in range(n):
                for z in range(n):
                    if graph[x][z] != True:
                        if max_num < graph[x][z]:
                            max_num = graph[x][z]
                            max_graph = [x,z]
            graph[x][y] == True
            student[arr[0]] = [x,y]
        else:
            #가장 많은값 찾기
            max(result1,key=result1.get)
            [result2.append(k) for k,v in result1.items() if max(result1.values()) == v] 
            max_num = 0
            for x,y in result2:
                if graph[x][y] > max:
                    result2.append([x,y])
        if len(result2) == 1:
            x,y = result2
            graph[x][y] == True
            student[arr[0]] = [x,y]
            continue
        else:
            result2.sort()
            x,y = result2[0][0],result2[0][1]
            graph[x][y] == True
            student[arr[0]] = [x,y]
            continue
