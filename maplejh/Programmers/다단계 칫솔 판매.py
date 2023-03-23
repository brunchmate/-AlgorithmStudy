# https://school.programmers.co.kr/learn/courses/30/lessons/77486
from collections import defaultdict


def solution(enroll, referral, seller, amount):
    answer = []
    refer = dict()
    money = defaultdict(int)
    for e, r in zip(enroll, referral):
        refer[e] = r
    for a, s in zip(amount, seller):
        price = a * 100
        while s != "-":
            if price < 10:
                money[s] += price
                break
            else:
                rate = price // 10
                money[s] += price - rate
                price = rate
                s = refer[s]
    for e in enroll:
        answer.append(money[e])
    return answer
