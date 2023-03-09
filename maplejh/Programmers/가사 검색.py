# https://school.programmers.co.kr/learn/courses/30/lessons/60060
from collections import defaultdict


def solution(words, queries):
    def make_trie(cur):
        for w in word:
            if '?' not in cur.keys():
                cur['?'] = 1
            else:
                cur['?'] += 1
            if w not in cur.keys():
                cur[w] = dict()
            cur = cur[w]
        cur["*"] = ''

    answer = []
    front_trie = defaultdict(dict)
    back_trie = defaultdict(dict)
    for word in words:
        n = len(word)
        make_trie(front_trie[n])
        word = word[::-1]
        make_trie(back_trie[n])
    for query in queries:
        n = len(query)
        if query[0] == '?':
            query = query[::-1]
            cur = back_trie[n]
        else:
            cur = front_trie[n]
        if not cur:
            answer.append(0)
            continue
        for q in query:
            if q not in cur.keys():
                answer.append(0)
                break
            cur = cur[q]
            if q == '?':
                answer.append(cur)
                break
    return answer
