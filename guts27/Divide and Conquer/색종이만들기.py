n = int(input())
blue = 0
white=0
paper = []
for _ in range(n):
    paper.append(list(map(int,input().split())))

def cut(x,y,n):
    global blue,white
    before = paper[x][y]
    flag = 0
    for i in range(x,x+n):
        for j in range(y,y+n):
            if before != paper[i][j]:
                cut(x,y,n//2)
                cut(x,y+n//2,n//2)
                cut(x+n//2,y,n//2)
                cut(x+n//2,y+n//2,n//2)
                return

    if before == 1:
        blue += 1
    else:
        white += 1

cut(0,0,n)
print(white)
print(blue)
