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

names = {}
cnt = 0
trie = Trie()

while sys.stdin:

    name = sys.stdin.readline().strip()

    if not name:
        break
    cnt += 1
    if trie.search(name):
        names[name] += 1
    else:
        trie.insert(name)
        names[name] = 1

names = sorted(names.items(), key=lambda x:x[0])

for n in names:
    print("%s %.4f" % (n[0], n[1] / cnt * 100))
