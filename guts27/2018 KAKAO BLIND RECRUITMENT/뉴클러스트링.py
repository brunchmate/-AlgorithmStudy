def solution(str1, str2):
    
    arr1 = []
    arr2 = []
    for i in range(0,len(str1)-1):
        if str1[i:i+2].isalpha():
            arr1.append(str1[i:i+2].lower())
    for i in range(0,len(str2)-1):
        if str2[i:i+2].isalpha():
            arr2.append(str2[i:i+2].lower())
    
    sarr1 = set(arr1)
    sarr2 = set(arr2)
    
    intersection = sarr1&sarr2
    union = sarr1 | sarr2
    if len(union) == 0 :
        return 65536
    intersection = sum([min(arr1.count(inter), arr2.count(inter)) for inter in intersection])
    union = sum([max(arr1.count(uni), arr2.count(uni)) for uni in union])
    answer = intersection / union * 65536
    return int(answer)
