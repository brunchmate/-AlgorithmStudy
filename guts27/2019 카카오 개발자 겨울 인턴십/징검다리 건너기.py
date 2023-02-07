# 제일 최초에 푼것은 정확성만 통과해서 다시 풀어야합니다.
# 최초에 푼 코드가 사라져서 대충 채워놨습니다.

def solution(stones, k):
    answer = 0
    jump = 0
    while True:
        for s in range(len(stones)):
            if stones[s] == 0:
                jump+=1
                if jump >= k:
                    return answer
            else:
                stones[s] -= 1
                if jump> 0:
                    jump = 0
        answer += 1
    
    
    # while True:
    #     min_num = min(stones[stones!=0])
    #     answer += min_num
    #     jump = 0
    #     for s in range(len(stones)):
    #         stones[s] -= min_num
    #         if stones[s] == 0:
    #             jump += 1
    #             if jump >= k:
    #                 return answer
    #         else:
    #             jump = 0        
    #     # 처음에 시간 초과가 나서 수정함
    
'''
문제해결 포인트  : 이진탐색
def solution(stones, k):
    answer = 0
    left = 1
    right = max(stones)
    
    while left <= right:
        count = 0
        mid = (left+right) // 2
        for s in stones:
            if s - mid <= 0:
                count += 1
            else:
                count = 0
            
            if count == k:
                break
        
        if count < k:
            left = mid +1
        else:
            right = mid -1
            answer = mid
        
    return answer
'''
