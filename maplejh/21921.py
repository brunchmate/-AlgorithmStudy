# https://www.acmicpc.net/problem/21921
import sys

input = sys.stdin.readline

N, X = map(int, input().split())
blog = list(map(int, input().split()))
visitor = sum(blog[:X])
max_visitor = visitor
cnt = 1
for i in range(X, N):
    visitor += (blog[i] - blog[i - X])
    if max_visitor < visitor:
        max_visitor = visitor
        cnt = 1
    elif max_visitor == visitor:
        cnt += 1
if max_visitor:
    print(max_visitor)
    print(cnt)
else:
    print("SAD")
