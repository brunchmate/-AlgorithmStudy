# https://school.programmers.co.kr/learn/courses/30/lessons/42893
# 정규표현식....
import re
from collections import defaultdict


def solution(word, pages):
    answer = 0
    word = word.lower()
    urls = defaultdict(str)  # index, url 매칭
    base = defaultdict(int)  # 기본 점수
    extra = defaultdict(float)  # 추가 점수
    for idx, p in enumerate(pages):
        urls[idx] = re.search(r'(<meta property.+content=")(https://\S+)"/>', p).group(2)  # 현재 url검색
        for f in re.findall(r'[a-zA-Z]+', p):  # 기본 점수 계산
            if f.lower() == word:
                base[idx] += 1
        lnk = re.findall(r'(a href=")(https://\S+)">', p)  # 현재 외부 링크들 검색
        for l in lnk:  # 추가 점수 계산
            extra[l[1]] += base[idx] / len(lnk)
    cur = 0
    for i in range(len(pages)):
        if cur < extra[urls[i]] + base[i]:
            cur = extra[urls[i]] + base[i]
            answer = i
    return answer
