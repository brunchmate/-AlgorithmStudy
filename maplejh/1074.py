# https://www.acmicpc.net/problem/1074
import sys

input = sys.stdin.readline

N, r, c = map(int, input().split())

ans = 0
for i in range(1, N + 1):
    cur = 2 ** (N - i)
    x, r = divmod(r, cur)
    y, c = divmod(c, cur)
    idx = x * 2 + y  # 몇 번째 사각형인지 체크
    ans += idx * cur ** 2  # 시작번호
print(ans)

'''
처음에 가장큰 사각형을 4등분 4등분한 사각형을 다시 4등분 ... 4등분한 사각형 하나의 크기가 1이 될때까지
각 사각형의 시작점은 0, 크기, 크기*2, 크기*3 번 째로 탐색을 한다.
'''