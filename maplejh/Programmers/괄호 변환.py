# https://school.programmers.co.kr/learn/courses/30/lessons/60058
def solution(p):
    def bracket(w):
        if not w:
            return w
        stack = 0
        correct = 1
        for i in range(len(w)):
            if w[i] == ')':
                stack -= 1
            else:
                stack += 1
            if stack == 0:
                break
            elif stack < 0:
                correct = 0
        u = w[:i + 1]
        v = w[i + 1:]
        if correct:
            return u + bracket(v)
        else:
            s = '(' + bracket(v) + ')'
            for k in u[1:-1]:
                if k == ')':
                    s += '('
                else:
                    s += ')'
            return s

    answer = bracket(p)
    return answer
