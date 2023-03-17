# https://school.programmers.co.kr/learn/courses/30/lessons/72414
def solution(play_time, adv_time, logs):
    def to_int(s):
        s = list(map(int, s.split(":")))
        return s[0] * 3600 + s[1] * 60 + s[2]

    def to_str(s):
        hh = str(s // 3600).zfill(2)
        mm = str((s % 3600) // 60).zfill(2)
        ss = str(s % 60).zfill(2)
        return ":".join([hh, mm, ss])

    play_time = to_int(play_time)
    adv_time = to_int(adv_time)
    log = [0] * (play_time + 1)
    for l in logs:
        l = l.split("-")
        start = to_int(l[0])
        end = to_int(l[1])
        log[start] += 1
        log[end] -= 1
    for i in range(1, play_time + 1):
        log[i] += log[i - 1]
    answer = 0
    max_watch = sum(log[:adv_time])
    watch = max_watch
    for start in range(1, play_time - adv_time + 1):
        watch -= log[start - 1]
        watch += log[start + adv_time - 1]
        if max_watch < watch:
            answer = start
            max_watch = watch
    return to_str(answer)
