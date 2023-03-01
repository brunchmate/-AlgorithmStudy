def search(n,number):
    temp = ''
    _dict = {10:'A',11:'B',12:'C',13:'D',14:'E',15:'F'}
    for num in range(0,number):
        temp2 = ''
        while True:
            q,r = divmod(num,n)
            num = q
            if r>=10:
                temp2+= _dict[r]
            else:
                temp2+=str(r)
            if q == 0:
                break
        temp+= temp2[::-1]
        if len(temp) >= number:
            break
    return temp
        
def solution(n, t, m, p):
    number = search(n,t*m+1)
    answer = ''
    i = 0
    for _ in range(t):
        answer += number[i+(p-1)]
        i = i+m
    
    return answer