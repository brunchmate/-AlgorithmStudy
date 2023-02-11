#규칙에 조건들 넣을때 꼼꼼하게 생각하기

def check2(place,x,y):
    dx,dy = [-1,0,1,0],[0,1,0,-1]
    dx2,dy2 = [-1,-1,1,1],[-1,1,1,-1]
    dx3,dy3 = [-2,0,2,0],[0,2,0,-2]
    
    for i in range(4):
        nx = x+dx[i]
        ny = y+dy[i]
        if 0>nx or nx>=5 or ny<0 or ny>=5:
            continue
        if place[nx][ny] == 'P':
            return False
    
    nx = x-1
    ny = y-1
    if 0<=nx<5 and 0<=ny<5:
        if place[nx][ny] == 'P':
            if place[x-1][y] != 'X' or place[x][y-1] != 'X':
                return False
    nx = x-1
    ny = y+1
    if 0<=nx<5 and 0<=ny<5:
        if place[nx][ny] == 'P':
            if place[x-1][y] != 'X' or place[x][y+1] != 'X':
                return False
    
    nx = x+1
    ny = y+1
    if 0<=nx<5 and 0<=ny<5:
        if place[nx][ny] == 'P':
            if place[x][y+1] != 'X' or place[x+1][y] != 'X':
                return False  
        
    nx = x+1
    ny = y-1
    if 0<=nx<5 and 0<=ny<5:
        if place[nx][ny] == 'P':
            if place[x][y-1] != 'X' or place[x+1][y] != 'X':
                return False  
    
    for i in range(4):
        nx = x+dx3[i]
        ny = y+dy3[i]
        if 0>nx or nx>=5 or ny<0 or ny>=5:
            continue 
        if place[nx][ny] != 'P':
            continue
        if place[x+dx[i]][y+dy[i]] =='X':
            continue
        else:
            return False
        
    return True

def check1(place):
    for j in range(5):
        for i in range(5):
            if place[i][j] == 'P':
                if not check2(place,i,j):
                    return False
    return True

def solution(places):
    answer = []
    
    for place in places:
        if check1(place):
            answer.append(1)
        else:
            answer.append(0)

    return answer
# def solution(places):
#     answer = []
#     def check(x,y,n):
#         place = places[n]
#         for i in range(x,5):
#             for j in range(5):
#                 if place[i][j] == 'P':
#                     distance = abs(x-i)+abs(y-j)
#                     if distance == 1:
#                         return 0
#                     elif distance <=2:
#                         if (i == x or j == y):
#                             if (i == x and j < y and place[i][j+1] != 'X') or (i == x and j > y and place[i][y+1] != 'X') or (i < x and j == y and place[i+1][y] != 'X') or (i > x and j == y and place[x+1][y] != 'X'):
#                                 return 0
#                         elif (i != x and j != y):
#                             if (i >x and (place[x+1][y] != 'X' or place[x][j] != 'X')) or (i < x and (place[x-1][y] != 'X' or place[x][j] != 'X')): return 0

#     for n in range(5):
#         bk = 'false'
#         for i in range(5):
#             for j in range(5):
#                 if places[n][i][j] == 'P':
#                     if check(i,j,n)==0:
#                         answer.append(0)
#                         bk = 'true'
#                         break
#             if bk == 'true':
#                 break
#         if bk == 'false':
#             answer.append(1)

#     return answer
