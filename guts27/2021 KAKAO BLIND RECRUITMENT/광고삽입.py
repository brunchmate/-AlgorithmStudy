def time2int(time):
    time = list(map(int,time.split(':')))
    return time[0]*3600 + time[1]*60 + time[2]
def int2time(num):
    q,r = divmod(num,3600)
    temp = str(q)
    q,r = divmod(r,60)
    return temp.zfill(2)+":"+str(q).zfill(2)+":" +str(r).zfill(2)
    return
def solution(play_time, adv_time, logs):
    answer = ''
    play_time = time2int(play_time)
    adv_time = time2int(adv_time)
    timelines = [0] * (play_time + 1)
    maxnum = -1
    
    for log in logs:
        log = log.split('-')
        start = time2int(log[0])
        end = time2int(log[1])
        timelines[start] += 1
        timelines[end] -= 1
        
    for i in range(1,play_time+1):
        timelines[i] = timelines[i] + timelines[i-1]
    for i in range(1,play_time+1):
        timelines[i] = timelines[i] + timelines[i-1]
        
    for i in range(adv_time-1,play_time):
        num = timelines[i] - timelines[i-adv_time]
        if num > maxnum:
            answer = i-adv_time +1
            maxnum = num
    return int2time(answer)
