# https://www.acmicpc.net/problem/1157
from collections import defaultdict
import sys

input = sys.stdin.readline

cnt = defaultdict(int)
word = input().strip()
for w in word:
    cnt[w.upper()] += 1
tmp = sorted(cnt.items(), key=lambda x: (-x[1], x[0]))[:2]
if len(tmp) == 1:
    print(tmp[0][0])
else:
    if tmp[0][1] == tmp[1][1]:
        print("?")
    else:
        print(tmp[0][0])
