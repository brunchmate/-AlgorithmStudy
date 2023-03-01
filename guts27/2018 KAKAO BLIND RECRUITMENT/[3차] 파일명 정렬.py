def solution(files):
    answer = []
    for i in range(len(files)):
        file = files[i]
        num = 0
        
        for j in range(len(file)):
            if file[j].isdigit():
                head = file[0:j]
                num = j
                break
        num2 = num
        # 
        for j in range(num,len(file)):
            if file[j].isdigit() == False or num2-num > 5:
                break
            num2 += 1
        number = int(file[num:num2])

        files[i] = [files[i], head.lower(),number]
    files.sort(key = lambda x : (x[1],x[2]))
    for file in files:
        answer.append(file[0])
    return answer