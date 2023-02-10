# https://school.programmers.co.kr/learn/courses/30/lessons/67257
from copy import deepcopy
from itertools import permutations


def solution(expression):
    def calculate(depth, flag):
        if depth == len(o):
            return
        if o[depth] == flag:
            if flag == '+':
                cn.append(cn.pop() + n[depth + 1])
            elif flag == '-':
                cn.append(cn.pop() - n[depth + 1])
            elif flag == '*':
                cn.append(cn.pop() * n[depth + 1])
        else:
            cn.append(n[depth + 1])
            co.append(o[depth])
        calculate(depth + 1, flag)

    answer = 0
    nums = []
    ops = []
    tmp = ''
    for exp in expression:
        if exp.isdigit():
            tmp += exp
        else:
            nums.append(int(tmp))
            tmp = ''
            ops.append(exp)
    nums.append(int(tmp))

    for p in permutations(set(ops)):
        n = deepcopy(nums)
        o = deepcopy(ops)
        for op in p:
            cn = [n[0]]
            co = []
            calculate(0, op)
            n = deepcopy(cn)
            o = deepcopy(co)
        answer = max(answer, abs(n[0]))
    return answer

# eval을 사용: 우선순위로 쪼갠다음 -> 합치면서 더함
def solution_v2(expression):
    answer = []
    ops = [['+', '-'], ['+', '*'], ['-', '+'], ['-', '*'], ['*', '+'], ['*', '-']]
    for a, b in ops:
        temp1 = []
        for e1 in expression.split(a):
            temp2 = []
            for e2 in e1.split(b):
                temp2.append(str(eval(e2)))
            temp1.append(str(eval(b.join(temp2))))
        answer.append(abs(eval(a.join(temp1))))

    return max(answer)
