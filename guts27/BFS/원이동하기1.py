import math
from collections import deque
N = int(input())
circle = []
for _ in range(N):
    x,y,r = map(int,input().split())
    circle.append([x,y,r])

print(circle)

#부모찾기
tree = dict()
for i in range(N):
    r1 = circle[i][2]
    x1,y1 = circle[i][0],circle[i][1]
    for j in range(i+1,N):
        r2 = circle[j][2]
        x2,y2 = circle[j][0],circle[j][1]
      # 두 원의 거리
        distance = math.sqrt((x1-x2)**2 + (y1-y2)**2)  
        # 내부에 있을 때
        if abs(r1-r2) >  distance:
            if tree[i+1]:
                tree[i+1] = (j, min(tree[i][2],abs(r1-r2)))
            else:
                tree[i+1] = (j+1,abs(r1-r2))

for i in range(1,N+1):
    ans = 0
    queue = deque()
    queue.append(i)
    # 부모 찾기
    # 부모가 있을겨우
    while queue: 
        n = queue.popleft()
        if tree[n] == n:
            break
        else:
            parent = tree[n]
            ans += 1
            queue.append(parent)
    # 나의 부모찾기가 끝나면 자기자신이 부모인 애중에 갈 수 있는곳이 있는지 체크
        #나를 부모로 가진 경우
    #부모가 없을 경우
          #나를 부모로 가진경우


