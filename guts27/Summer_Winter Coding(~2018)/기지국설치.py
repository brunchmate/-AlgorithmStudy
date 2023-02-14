def solution(n, stations, w):
    answer = 0
    now = 0
    for s in stations:
        length = s-w-1
        answer += (length-now)//(2*w+1)
        if (length-now)%(2*w+1) != 0:
            answer += 1
        now = s+w
    answer +=  ((n-now)//(2*w+1))
    if ((n-now)%(2*w+1)) != 0:
        answer += 1

    return answer