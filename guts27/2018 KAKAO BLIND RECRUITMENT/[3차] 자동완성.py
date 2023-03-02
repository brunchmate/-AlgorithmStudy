def solution(words):
    answer = 0
    arr = [0]*len(words)
    words.sort()
    for i in range(len(words)):
        if i == len(words)-1:
            end = i
        else:
            end = i+2
        for j in range(i-1,end):
            if i ==j :
                continue
            if  words[i] in words[j]:
                arr[i] = len(words[i])
            else:
                point = -1
                y = min(len(words[i]),len(words[j]))
                for x in range(0,y):
                    if words[i][x] == words[j][x]:
                        point = x
                    else:
                        break
                if point == -1:
                    arr[i] = max(arr[i], 1)
                else:
                    arr[i] = max(arr[i], point+2)

    return sum(arr)
