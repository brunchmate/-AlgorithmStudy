def binary(num,n):
    temp = ''
    for _ in range(n):
        q,r = divmod(num,2)
        temp = temp + str(r)
        num = q
    return temp[::-1]
def solution(n, arr1, arr2):
    answer = []
    
    for i in range(n):
        a1 = binary(arr1[i],n)
        a2 = binary(arr2[i],n)
        temp = ''
        for i in range(n):
            if a1[i] == '0' and a2[i] == '0':
                temp = temp + ' '
            else:
                temp += '#'
        answer.append(temp)
    return answer

def solution(n, arr1, arr2):
    answer = []
    for i,j in zip(arr1,arr2):
        a12 = str(bin(i|j)[2:])
        a12=a12.rjust(n,'0')
        a12=a12.replace('1','#')
        a12=a12.replace('0',' ')
        answer.append(a12)
    return answer