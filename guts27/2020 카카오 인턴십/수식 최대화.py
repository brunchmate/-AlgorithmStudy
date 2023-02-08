import copy

def solution(expression):
    answer = 0
    operator = [['+','-','*'],['+','*','-'],['-','+','*'],['-','*','-'],['*','-','+'],['*','+','-']]
    expression = expression.replace('-', ' - ')
    expression = expression.replace('+', ' + ')
    expression = expression.replace('*', ' * ')
    expression = expression.split(' ')
    for oper in operator:
        temp = copy.deepcopy(expression)
        for i in range(3):
            if temp.count(oper[i]) == 1:
                indx = temp.index(oper[i])
                cal = temp[indx-1]+temp[indx]+temp[indx+1]
                cal = str(eval(cal))
                del temp[indx-1:indx+2]
                temp.insert(indx-1, cal)
            elif temp.count(oper[i]) > 1:
                for _ in range(temp.count(oper[i])):
                    indx = temp.index(oper[i])
                    cal = temp[indx-1]+temp[indx]+temp[indx+1]
                    cal = str(eval(cal))
                    del temp[indx-1:indx+2]
                    temp.insert(indx-1, cal)
        answer = max(answer, abs(int(temp[0])))

    return answer
