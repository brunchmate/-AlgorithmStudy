def solution(survey, choices):
    answer = ''
    degree = {1:3,2:2,3:1}
    agree = {5:1,6:2,7:3}
    dic = {"A":0,"N":0,"J":0,"M":0,"C":0,"F":0,"R":0,"T":0}
    arr = [("R","T"),("C","F"),("J","M"),("A","N")]

    for s,c in zip(survey, choices):
        if c == 4:
            continue
        if c in agree:
            dic[s[1]] += agree[c]
        else:
            dic[s[0]] += degree[c]

    for x,y in arr:
        if dic[x] >= dic[y]:
            answer += x
        elif dic[x] <dic[y]:
            answer += y
    
    return answer
