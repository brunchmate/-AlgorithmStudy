'''
def check(key,length,lock):
    global zcount
    cnt = zcount
    for i in range(length):
        for j in range(length):
            if key[i][j] == 1 and lock[i][j] == 1:
                return False
            elif key[i][j] == 1 and lock[i][j] == 0:
                cnt+=1
    if cnt == zcount:
        return True
    else:
        return False
def move(key,length,lock):
    i = 0
    while i < length:
        for i in range(length):
            for j in reversed(range(length)):
                if j == 0:
                    key[i][j] = 0
                else:
                    key[i][j] = key[i][j-1]
        key2 = [arr[:] for arr in key]
        if check(key2,length,lock):
            return True
        while i < length:
            for i in reversed(range(length)):
                if  i ==0:
                    key2[i] = [0 for _ in range(length)]
                else:
                    key2[i] = key[i-1]
            if check(key2,length,lock):
                return True
    return False
                
def solution(key, lock):
    answer = True
    global zcount
    zcount = lock.count(0)
    length = len(lock)
    move(key,length,lock)
    # rotate
    for _ in range(4):
        new_key = [[0] * length for _ in range(length)]
        for i in range(length):
            for j in range(length):
                new[j][length-i-1] = key[i][j]
        if move(new_key,length,lock):
            return 'true'
    return 'false'
'''
