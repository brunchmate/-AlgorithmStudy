import math

def solution(numbers, hand):
    answer = ''
    #인덱스 값 넣을때 조심
    left = [3,0]
    right = [3,2]
    keypad = [[3,1],[0,0],[0,1],[0,2],[1,0],[1,1],[1,2],[2,0],[2,1],[2,2]]
    for num in numbers:
        if num in [1,4,7]:
            left = keypad[num]
            answer += 'L'
        elif num in [3,6,9]:
            right = keypad[num]
            answer += 'R'
        else:
            a = keypad[num][0]
            b = keypad[num][1]
            l = abs(a-left[0])+abs(b-left[1])
            r = abs(a-right[0])+abs(b-right[1])
            if l > r or (l==r and hand == 'right'):
                right = keypad[num]
                answer += 'R'
            elif r > l or (l==r and hand == 'left'):
                left = keypad[num]
                answer += 'L'
                    
    return answer
