import math
from itertools import combinations
def is_prime_number(x):
    #파이썬 제곱근 기본방식: 숫자**(1/2)
    for i in range(2, int(math.sqrt(x)) + 1):
        if x % i == 0:
            return False 
    return True 
def solution(nums):
    answer = 0
    for i in combinations(nums,3):
        if is_prime_number(sum(i)):
            answer += 1

    return answer

https://freedeveloper.tistory.com/391