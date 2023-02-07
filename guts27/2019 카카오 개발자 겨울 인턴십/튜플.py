def solution(s):
    answer = []
    num = []
    s= s[1:-1]
    start = 0
    end = 0
    for i in range(len(s)):
        # S = S[2:-2].split("},{")
		#list(map(int, s.replace("{", "").replace("}", "").split(",")))
        if s[i] == '{':
            start = i
            continue
        if s[i] == '}':
            end = i
            num.append(list(map(int, s[start+1:end].split(','))))
    #길이 순으로 정렬
    num.sort(key=len)
    for n in num:
        for z in n:
            if z not in answer:
                answer.append(z)
    return answer
