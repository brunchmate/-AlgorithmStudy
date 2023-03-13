import re
def solution(words, queries):
    answer = []
    for q in queries:
        q = q.replace('?','.')
        p = re.compile(q)
        length = len(q)
        num = 0
        for word in words:
            m = p.match(word)
            if m == None:
                continue
            elif len(word) == length:
                num+=1
        answer.append(num)
    return answer
