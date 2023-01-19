import sys

sys.setrecursionlimit(10 ** 7)

T = int(input())
students = [[0]*100000 for _ in range(T)]

student = []
for t in range(T):
    student.append(int(input()))
    students[t] = [0] +list(map(int,input().split()))

def dfs(x,t):
    global result
    visited[x] = True
    cycle.append(x)
    choice = students[t][x]
    if visited[choice] == True:
        if choice in cycle:
            result += cycle[cycle.index(choice):]
        return 
    else:
        dfs(choice,t)

for t in range(T):
    t =t
    result = []
    visited = [0]*(student[t]+1)
    for i in range(1, student[t]+1):
        if visited[i] == False:
            cycle = []
            dfs(i,t)
    print(student[t] - len(result))
    
    ##포인트: 사이클 생성
