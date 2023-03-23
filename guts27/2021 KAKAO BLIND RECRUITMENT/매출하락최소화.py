def find(root,dic,arr):
    min_num = dic[root]
    key = root
    for a in arr[root]:
        if min_num > dic[a]:
            min_num = dic[a]
            key = a
    return min_num,key
def solution(sales, links):
    answer = 0
    arr2 = []
    dic = {}
    for i in range(len(sales)):
        dic[i+1] = sales[i]
    arr = [[] for _ in range(len(sales)+1)]
    for x,y in links:
        arr[x].append(y)
    num = 0
    
    for i in range(1,len(arr)):
        if len(arr[i]) == 0:
            continue
        min1,key = find(i,dic,arr)
        for a in arr[i]:
            if len(arr[a]) != 0 :
                min2,key2 = find(a,dic,arr)
                if dic[a] < min1+min2:
                    arr2.append((dic[a],a))
                else:
                    arr2.append((min1,key))
                    arr2.append((min2,key2))

    for x,y in arr2:
        answer+=x
    return answer
