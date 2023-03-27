def solution(id_list, report, k):
    answer = [0 for _ in range(len(id_list))]
    dic = {}
    arr = [[] for _ in range(len(id_list))]
    for i in range(len(id_list)):
        dic[id_list[i]] = i
    
    for re in report:
        a,b = re.split(' ')
        if a not in arr[dic[b]]:
            arr[dic[b]].append(a)

    for i in range(len(arr)):
        if len(arr[i]) >= k:
            for j in arr[i]:
                answer[dic[j]] += 1
    return answer