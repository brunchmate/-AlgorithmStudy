def bonus(num,_bonus):
    if _bonus == "D":
        return num * num
    elif _bonus == "T":
        return num * num * num
    return num
def option(_option,arr):
    if _option == "*":
        if len(arr) == 1:
            arr[-1] = arr[-1]*2
        else:
            arr[-1] = arr[-1]*2
            arr[-2] = arr[-2]*2
    else:
        arr[-1] = arr[-1] * (-1)
def solution(dartResult):
    i = 0
    global arr
    arr= []
    while i < len(dartResult):
        if dartResult[i+1] == '0':
            num = 10
            _bonus = dartResult[i+2]
            i = i+3
        else:
            num = int(dartResult[i])
            _bonus = dartResult[i+1]
            i += 2
        arr.append(bonus(num,_bonus))
        if i>=len(dartResult):
            break
        if dartResult[i].isdigit() == False:
            _option = dartResult[i]
            i += 1
            option(_option,arr)
    return sum(arr)