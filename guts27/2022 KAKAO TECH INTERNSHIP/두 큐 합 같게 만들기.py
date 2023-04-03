from collections import deque

def solution(queue1, queue2):
    answer = -1
    goal = sum(queue1) + sum(queue2) // 2
    sum1=sum(queue1)
    sum2 = sum(queue2)
    queue1 = deque(queue1)
    queue2 = deque(queue2)
    length = len(queue1)
    num = 0
    while sum1 != sum2:
        if sum1 >sum2:
            p1 = queue1.popleft()
            queue2.append(p1)
            sum1 -=p1
            sum2 += p1
        else:
            p1 = queue2.popleft()
            queue1.append(p1)
            sum1 += p1
            sum2 -= p1
        num+=1
        if num > length*3:
            return answer
    # if num:
    #     return num
    return num
