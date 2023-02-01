n, r, c = map(int, input().split(' '))
result = 0

def cut(n, x, y):
    global result
    if x == r and y == c:
        print(int(result))
        return #exit(0)

    if n == 1:
        result += 1
        return

    if not (x <= r < x + n and y <= c < y + n):
        result += n * n
        return
    cut(n / 2, x, y)
    cut(n / 2, x, y + n / 2)
    cut(n / 2, x + n / 2, y)
    cut(n / 2, x + n / 2, y + n / 2)

cut(2 ** n, 0, 0)

## 문제를 잘 쪼개야한다.
