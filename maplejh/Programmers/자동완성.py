# https://school.programmers.co.kr/learn/courses/30/lessons/17685
def solution(words):
    answer = 0
    trie = dict()
    for word in words:
        cur = trie
        for w in word:
            answer += 1
            if w not in cur.keys():
                cur[w] = dict()
            cur = cur[w]
        cur['*'] = ''

    for word in words:
        cnt = 0
        cur = trie
        for w in word:
            if len(cur[w]) == 1:
                if "*" not in cur[w].keys():
                    cnt += 1
            else:
                cnt = 0
            cur = cur[w]
        answer -= cnt
    return answer
