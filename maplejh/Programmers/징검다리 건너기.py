# https://school.programmers.co.kr/learn/courses/30/lessons/64062
import heapq

# 슬라이딩 윈도우
def solution(stones, k):
    answer = max(stones[:k])
    start = 0
    q = []
    visited = [0] * len(stones)
    for end in range(len(stones)):
        heapq.heappush(q, (-stones[end], end))
        visited[end] = 1
        if end - start == k:
            visited[start] = 0
            while not visited[q[0][1]]:
                cur, idx = heapq.heappop(q)
            start += 1
            answer = min(-q[0][0], answer)
    return answer
