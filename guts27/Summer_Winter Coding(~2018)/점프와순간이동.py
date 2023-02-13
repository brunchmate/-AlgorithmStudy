def solution(n):
    count = 0
    while n > 0:
        q,r = divmod(n,2)
        n = q
        if r != 0:
            count += 1
    return count