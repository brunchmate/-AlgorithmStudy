# https://www.acmicpc.net/problem/7662
import sys
import heapq

input = sys.stdin.readline

T = int(input())
for _ in range(T):
    k = int(input())
    min_q = []
    max_q = []
    rm = [0] * k
    for i in range(k):
        cmd, n = input().split()
        if cmd == "I":
            rm[i] = 1
            heapq.heappush(min_q, (int(n), i))
            heapq.heappush(max_q, (-int(n), i))
        else:
            if int(n) == 1:
                while max_q:
                    _, cur = heapq.heappop(max_q)
                    if rm[cur]:
                        rm[cur] = 0
                        break
            elif int(n) == -1:
                while min_q:
                    _, cur = heapq.heappop(min_q)
                    if rm[cur]:
                        rm[cur] = 0
                        break
    ans = []
    while max_q:
        x, cur = heapq.heappop(max_q)
        if rm[cur]:
            ans.append(-x)
            break
    while min_q:
        x, cur = heapq.heappop(min_q)
        if rm[cur]:
            ans.append(x)
            break
    if ans:
        print(*ans)
    else:
        print("EMPTY")
