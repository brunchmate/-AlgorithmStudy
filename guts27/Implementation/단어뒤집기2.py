string = input()
p = -1
flag = False
result = ""
for i in range(len(string)):
    s = string[i]
    if flag:
        continue
    if s == "<":
        flag = True
        continue
    if s == ">":
        flag = False
        continue
    if p==-1:
        p = i
    if p != -1 and s == " ":
        temp = string[p:i]
        result = result + string[len(result)-1: p] + temp[::-1] + " "
        p = -1
if len(result) != len(string):
    if p != 0:
        temp = string[p:]
        result = result + temp[::-1]
    else:
        result = result + string[len(result)-1:]
print(result)