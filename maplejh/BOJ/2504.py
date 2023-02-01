# https://www.acmicpc.net/problem/2504
import sys

input = sys.stdin.readline

ss = input()
stack = []
ans = 0
tmp = 1
prior = 1
for s in ss:
    if s == "(":
        if prior != 1:
            ans += tmp
            tmp //= prior
            prior = 1
        tmp *= 2
        stack.append(s)
    elif s == "[":
        if prior != 1:
            ans += tmp
            tmp //= prior
            prior = 1
        tmp *= 3
        stack.append(s)
    elif s == ")":
        if stack and stack[-1] == "(":
            stack.pop()
            prior *= 2
        else:
            ans = 0
            break
    elif s == "]":
        if stack and stack[-1] == "[":
            stack.pop()
            prior *= 3
        else:
            ans = 0
            break
else:
    if not stack:
        ans += tmp
    else:
        ans = 0
print(ans)

'''
분배법칙처럼 이용
((()))처럼 마지막 괄호안에는 아무것도 없도록 (()[]) 이건 나눠진게 아님
(()[[]])([])
->(())+([[]])+([]) 이런식으로 세트로 나눈다고 생각
->2*2 + 2*3*3 + 2*3
(,[ 이면 2나3을 곱하고
),] 이면 처음으로 하나의 세트가 만들어지는 것이므로 다른 세트에 영향을 안주도록 사라지는 (나 [는 지워줌 -> 2나 3으로 나눠줌
다시 (,[ 이 나오면 새로운 세트가 시작하는 것이므로 이전의 세트의 값들을 구해서 더함
'''