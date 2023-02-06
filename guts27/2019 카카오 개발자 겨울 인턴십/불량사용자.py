import re
from itertools import permutations

def check(a,b):
    length = len(b)
    ban = b.replace('*','.')
    ban = re.compile(ban)
    m= ban.match(a)
    if m and length == len(a):
        return True
    else:
        return False
def solution(user_id, banned_id):
    answer = []

    for perm in (permutations(user_id,len(banned_id))):
        count = 0
        for a,b in zip(perm,banned_id):
            if check(a,b):
                count+=1
                
        if count == len(banned_id):
            if set(perm) not in answer:
                answer.append(set(perm))

    return len(answer)
