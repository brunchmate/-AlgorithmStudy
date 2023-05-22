students = [False for _ in range(31)]
for _ in range(28):
    students[int(input())] = True
for i in range(1,31):
    if students[i] != True:
        print(i)