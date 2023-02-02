import sys

class Node(object):
    def __init__(self,key):
        self.key=key
        self.child={}

class Trie(object):
    def __init__ (self):
        self.head = Node(None)

    def insert(self,word):
        cur = self.head

        for ch in word:
            if ch not in cur.child:
                cur.child[ch] = Node(ch)
            cur =cur.child[ch]
        cur.child['*'] = True

    def search(self,word):
        cur = self.head

        for ch in word:
            if ch not in cur.child:
                return False
            cur = cur.child[ch]

        if '*' in cur.child:
            return True
cnt = 0
trie = Trie()
n,m = map(int,sys.stdin.readline().split())
for _ in range(n):
    trie.insert(sys.stdin.readline().strip())
for _ in range(m):
    if trie.search(sys.stdin.readline().strip()):
        cnt+=1

print(cnt)
