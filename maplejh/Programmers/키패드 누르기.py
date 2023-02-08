# https://school.programmers.co.kr/learn/courses/30/lessons/67256
def solution(numbers, hand):
    answer = ''
    phone = {1: (0, 0), 2: (0, 1), 3: (0, 2), 4: (1, 0), 5: (1, 1), 6: (1, 2), 7: (2, 0), 8: (2, 1), 9: (2, 2),
             0: (3, 1)}
    r = [3, 2]
    l = [3, 0]
    for n in numbers:
        nx, ny = phone[n]
        if n in [1, 4, 7]:
            answer += 'L'
        elif n in [3, 6, 9]:
            answer += 'R'
        else:
            dist1 = abs(r[0] - nx) + abs(r[1] - ny)
            dist2 = abs(l[0] - nx) + abs(l[1] - ny)
            if dist1 > dist2:
                answer += 'L'
            elif dist1 < dist2:
                answer += 'R'
            else:
                answer += hand[0].upper()
        if answer[-1] == 'L':
            l = [nx, ny]
        else:
            r = [nx, ny]
    return answer
