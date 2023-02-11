#Node 정의
class Node:
    def __init__(self, data, next=None):  #data 만 입력시 next 초기값은 None이다.
        self.data = data #다음 데이터 주소 초기값 = None
        self.next = next
https://ybworld.tistory.com/85
https://dean30.tistory.com/93
https://comdoc.tistory.com/entry/2021-%EC%B9%B4%EC%B9%B4%EC%98%A4-%EC%B1%84%EC%9A%A9%EC%97%B0%EA%B3%84%ED%98%95-%EC%9D%B8%ED%84%B4%EC%8B%AD-%ED%91%9C-%ED%8E%B8%EC%A7%91
https://gingerkang.tistory.com/125


def solution(n, k, cmd):
    answer = ['O']*n
    delete = []
    d = dict()
    for i in range(n):
        d[i] = i
    for c in cmd:
        a,b = c[0],c[-1]
        if a== 'U':
            k = k-int(b)
        elif a== 'D':
            k = k+int(b)
        elif a == 'C':
            delete.append(d[k])
            for z in range(k,n-1):
                d[z] = d[z+1]
            del d[n-1]
            n = n-1
            if k == n:
                k -= 1
        else:
            d[n] = delete.pop()
            n = n+1
    
    for i in delete:
        answer[i] = 'X'
    return ''.join(answer)
