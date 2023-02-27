# https://school.programmers.co.kr/learn/courses/30/lessons/17678
def solution(n, t, m, timetable):
    def time_to_int(s):
        s = s.split(":")
        return int(s[0]) * 60 + int(s[1])

    timetable.sort()
    q = dict()
    latest = dict()
    for i in range(n):
        q[540 + t * i] = m
        latest[540 + t * i] = 540 + t * i
    for tt in timetable:
        tt = time_to_int(tt)
        for k in sorted(q.keys()):
            if q[k] and tt <= k:
                q[k] -= 1
                if not q[k]:
                    latest[k] = tt - 1
                break
    corn = latest[540 + t * (n - 1)]
    hh, mm = map(str, divmod(corn, 60))
    return f'{hh.zfill(2)}:{mm.zfill(2)}'
