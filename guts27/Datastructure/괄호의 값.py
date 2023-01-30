# brackets = input()
# last = ''
# answer = 0
# temp = []
# cnt = 0
# for now in range(len(brackets)):
    
#     if brackets[now] == '(':
#         temp.append('(')
#     elif brackets[now] == '[':
#         temp.append('[')
#     elif brackets[now] == ')':
#         if temp[-1] == '[':
#             print(0)
#             break
#         del temp[-1]
#         if cnt == 0:
#             cnt = 2
#         elif last == '(':
#             cnt *= 2
#         else:
#             answer += cnt
#             cnt = 2
#         last = '('
#     elif brackets[now] == ']':
#         if temp[-1] == '(':
#             print(0)
#             break
#         del temp[-1]
#         if cnt == 0:
#             cnt = 3
#         elif last == '[':
#             cnt *= 3
#         else:
#             answer += cnt
            
            
#             cnt = 3
#         last = '['

# print(answer)
