# https://school.programmers.co.kr/learn/courses/30/lessons/60062
import heapq


def solution(n, weak, dist):
    dist.sort(reverse=True)
    q = [(0, tuple(weak))]  # cnt, 남은 취약점 수
    state = set()  # 탐색할 취약점들 튜플 (->이미 적은 사람으로 탐색함, cnt가 더 클때 탐색할 필요없음)
    state.add(tuple(weak))
    while q:
        cnt, todo = heapq.heappop(q)
        if cnt >= len(dist):
            return -1
        d = dist[cnt]
        for s in todo:
            e = (s + d) % n
            tmp = []  # 시작점이 s일때 거리 d로 탐색하지 못하는 취약점들
            if s < e:
                for t in todo:
                    if s > t or e < t:
                        tmp.append(t)
            else:
                for t in todo:
                    if e < t < s:
                        tmp.append(t)
            if not tmp:
                return cnt + 1
            tmp = tuple(tmp)
            if tmp in state:
                continue
            state.add(tmp)
            heapq.heappush(q, (cnt + 1, tmp))
