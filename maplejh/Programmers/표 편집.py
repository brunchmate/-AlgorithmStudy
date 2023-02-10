# https://school.programmers.co.kr/learn/courses/30/lessons/81303
def solution(n, k, cmd):
    answer = ["O"] * n
    lnk = dict()
    for i in range(-1, n + 1):
        lnk[i] = [i - 1, i + 1]
    ds = []  # delete stack
    for c in cmd:
        c = c.split()
        if c[0] == "U":
            for _ in range(int(c[1])):
                k = lnk[k][0]
        elif c[0] == "D":
            for _ in range(int(c[1])):
                k = lnk[k][1]
        elif c[0] == "C":
            ds.append(k)
            lnk[lnk[k][0]][1] = lnk[k][1]
            lnk[lnk[k][1]][0] = lnk[k][0]
            if lnk[k][1] == n:
                k = lnk[k][0]
            else:
                k = lnk[k][1]
        elif c[0] == "Z":
            dx = ds.pop()
            lnk[lnk[dx][0]][1] = dx
            lnk[lnk[dx][1]][0] = dx
    for d in ds:
        answer[d] = "X"
    return ''.join(answer)
