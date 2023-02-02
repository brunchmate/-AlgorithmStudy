# https://www.acmicpc.net/problem/21318
import sys

input = sys.stdin.readline

N = int(input())
music = list(map(int, input().split()))
prefix = [0] * N  # 1일 ~ N-1일 까지 실수 누적합
for idx in range(1, N):
    prefix[idx] = prefix[idx - 1]
    if music[idx - 1] > music[idx]:
        prefix[idx] += 1

Q = int(input())
for _ in range(Q):
    x, y = map(int, input().split())
    print(prefix[y - 1] - prefix[x - 1])  # 구간의 마지막 날은 실수 X -> 마지막 전 날까지 실수
