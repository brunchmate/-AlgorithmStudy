from collections import deque
def solution(food_times, k):
    answer = 0
    j = 0
    queue = deque()
    for idx,time in enumerate(food_times):
        queue.append((time,idx+1))
    for _ in range(k):
        if len(queue) == 0:
            return -1
        time, idx = queue.popleft()
        time -= 1
        if time == 0:
            continue
        queue.append((time,idx))
    if len(queue) == 0:
        return -1
    answer = queue.popleft()
    return answer[1]
