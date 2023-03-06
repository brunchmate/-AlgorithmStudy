def solution(s):
    length = len(s)
    answer = length
    for i in range(1, length//2+1):
        num = 1
        tmp= ''
        for j in range(0,length,i):
            if s[j:j+i] == s[(j+i):(j+2*i)]:
                num+=1
            else:
                if num == 1:
                    tmp =  tmp + s[j:j+i]
                else:
                    tmp =  tmp + str(num) + s[j:j+i]
                    num = 1
        answer = min(answer,len(tmp))
    return answer
