from itertools import combinations

def solution(relation):
    row = len(relation)
    col = len(relation[0])  

    # 가능한 column 조합 생성
    candidates=[]
    for i in range(1,col+1):
        candidates.extend(combinations(range(col),i))

    # 유일성
    unique = []
    for candi in candidates:
        arr = set()
        for i in range(row):
            temp = []
            for j in range(len(candi)):
                temp.append(relation[i][candi[j]])
            arr.update(temp)
        if len(arr) == row:
            unique.append(candi)
            #extend nono
            
    # 최소성
    answer = set(unique)
    for i in range(len(unique)):
        for j in range(len(unique)):
            if i==j:
                continue
            if len(unique[i]) == len(set(unique[i]) && set(unique[j])):
                answer.discard(unique[j])
    return len(answer)
