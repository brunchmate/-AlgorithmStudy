import math

# 소수 판별 함수
def is_prime_number(x):
    if x == 1:
        return False
    # 2부터 x의 제곱근까지의 모든 수를 확인하며
    for i in range(2, int(math.sqrt(x)) + 1):
        # x가 해당 수로 나누어떨어진다면
        if x % i == 0:
            return False # 소수가 아님
    return True # 소수임
def n2k(n,k):
    T = "0123456789ABCDEF"
    temp = ""
    while n > 0:
        n,r = divmod(n,k)
        temp = T[r]+temp
    return temp    
 
def solution(n, k):
    answer = 0
    zero = 0
    start = 0
    temp = n2k(n,k)
    
    for i in range(len(temp)):
        if temp[i] == '0':
            if zero == 0:
                zero = 1
                start = i+1
            else:
                if i == start:
                    start = i+1
                else:
                    if is_prime_number(int(str(temp[start:i]), 10)):
                        answer += 1
                    start = i+1

    if zero == 0:
        if is_prime_number(int(str(temp), 10)):
            answer += 1
    
    start = 0
    for i in range(len(temp)):
        if temp[i] == "0" and start < i:
            if is_prime_number(int(str(temp[start:i]), 10)):
                answer += 1
                break

    end = len(temp)-1
    if temp[end] == '0':
        return answer
    for i in range(len(temp)-1,0,-1):
        if temp[i] == '0' and i < end:
            if is_prime_number(int(str(temp[i+1:]), 10)):
                answer += 1
                break

    return answer

