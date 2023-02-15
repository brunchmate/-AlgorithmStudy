def solution(dirs):
    x,y = 0,0
    answer = 0
    road = []
    for dir in dirs:
        if dir == "U" and y+1 <= 5:
            nx, ny = x,y+1
        elif dir == "D" and y-1 >= -5:
            nx, ny = x,y-1
        elif dir == "R" and x+1 <=5:
            nx, ny = x+1,y
        elif dir == "L" and x-1 >=-5:
            nx, ny = x-1,y
        else:
            continue

        if (x,y,nx, ny) not in road:
            road.append((x,y,nx, ny))
            road.append((nx, ny,x,y))
            answer += 1
        x= nx
        y = ny
    return answer
    return answer
