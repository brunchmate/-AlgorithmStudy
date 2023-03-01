def solution(msg):
    answer = []
    _dict = {'A': 1, "B":2 , "C":3,"D":4,
             "E":5,"F":6,"G":7,"H":8,"I":9,"J":10,"K":11,"L":12,"M":13,"N":14,"O":15,"P":16,"Q":17,"R":18,"S":19,"T":20,"U":21,"V":22,"W":23,"X":24,"Y":25,"Z":26}
    i = 0
    num=1
    while i <len(msg):
        while True:
            print(msg[i:num])
            if msg[i:num] in _dict and num <= len(msg):
                num+=1
            else:
                break
        answer.append(_dict[msg[i:num-1]])
        _dict[msg[i:num]]=len(_dict)+1
        i = num-1
    return answer