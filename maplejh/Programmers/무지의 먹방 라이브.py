# https://school.programmers.co.kr/learn/courses/30/lessons/42891
import heapq


def solution(food_times, k):
    q = []
    for i, f in enumerate(food_times):
        heapq.heappush(q, (f, i))
    n = len(food_times)
    r = 0  # 현재 몇 라운드인지
    left = n  # 현재 남은 음식 개수
    zero = [0] * n  # 다 먹었는지 체크
    # 항상 0 부터
    while q:
        min_f, idx = heapq.heappop(q)
        min_f -= r
        if k < left * min_f:
            k %= left
            # 나머지 값들 처리
            cur = 0
            while k:
                if not zero[cur]:
                    zero[cur] = 1
                    k -= 1
                cur = (cur + 1) % n
            break
        else:
            k -= left * min_f
            zero[idx] = 1
            r += min_f
            left -= 1
    else:
        return -1
    # 네트워크 장애 다음 차례 찾기
    for ans in range(cur, n):
        if not zero[ans]:
            return ans + 1
