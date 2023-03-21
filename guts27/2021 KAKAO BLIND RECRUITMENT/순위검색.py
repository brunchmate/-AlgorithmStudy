from bisect import bisect_left
def solution(info, query):
    answer = []
    arr = []
    diction = {}
    for i in info:
        a,b,c,d,e = i.split()
        arr.append([a,'-'])
        arr.append([b,'-'])
        arr.append([c,'-'])
        arr.append([d,'-'])
        e = int(e)

        cases = [[f,g,h,i] for f in [a,'-'] for g in [b,'-'] for h in [c,'-'] for i in [d,'-']] 
        for cas in cases:
            string = ''.join(cas)
            if string in diction: 
                diction[string].append(e)
            else:
                diction[string] = [e]
                
    for key in diction.keys():
        diction[key].sort()
        
    for q in query:
        q = q.replace(" and "," ")
        q = q.split(" ")
        string = q[0] + q[1] + q[2] + q[3]
        
        if string in diction:
            answer.append(len(diction[string]) - bisect_left(diction[string],int(q[4])))
        else:
            answer.append(0)
    return answer
