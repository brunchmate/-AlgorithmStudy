# https://school.programmers.co.kr/learn/courses/30/lessons/64064

# trie 알고리즘
def solution(user_id, banned_id):
    def search(tree, depth, string):
        if depth == len(bid):
            if 'A' in tree:
                tmp.append(string)
            return
        for key in tree.keys():
            if key == bid[depth] or bid[depth] == '*':
                search(tree[key], depth + 1, string + key)

    def match(depth):
        if depth == len(banned_id):
            answer.add(tuple(visited.values()))
            return
        for x in candidate[depth]:
            if not visited[x]:
                visited[x] = 1
                match(depth + 1)
                visited[x] = 0

    answer = set()
    trie = {}
    visited = dict()
    for uid in user_id:
        root = trie
        visited[uid] = 0
        for u in uid:
            if u not in root:
                root[u] = {}
            root = root[u]
        root['A'] = {}
    candidate = []
    for bid in banned_id:
        tmp = []
        search(trie, 0, '')
        candidate.append(tmp)
    match(0)
    return len(answer)


# permutation으로도 가능