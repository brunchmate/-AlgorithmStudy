def solution(n, t, m, timetable):
    answer = ''
    for ti in range(len(timetable)):
        temp = timetable[ti].split(':')
        timetable[ti] = int(temp[0])*60 + int(temp[1])
    arr = []
    
    # 셔틀버스 시간 담기
    end = (n-1) *t
    for i in range(0,end+1,t):
        temp = 9*60 + i
        arr.append(temp)
    
    # 승객수
    count = m
    timetable.sort()
    # 셔틀 버스 횟수
    length = n
    end = 0
    for ar in range(len(arr)):
        count = m
        for ti in range(len(timetable)):
            if arr[ar] >= timetable[ti] and timetable[ti] != -1:
                if count ==0:
                    break
                count-=1
                end =  timetable[ti]
                timetable[ti] = -1
                    
        length -= 1
        if length ==0:
            break
    if length == 0 and count == 0:
        r,q = divmod(end-1, 60)
        return str(r).zfill(2)+':'+str(q).zfill(2)
        
    r,q = divmod(arr[-1], 60)
    return str(r).zfill(2)+':'+str(q).zfill(2)
