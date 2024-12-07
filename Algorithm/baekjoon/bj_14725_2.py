import sys; input = sys.stdin.readline


def insert(words):
    now = trie
    for word in words:
        now = now.setdefault(word, dict())

def sout(now,level=0):
    for word in sorted(now):
        print("--"*level+word)
        sout(now[word], level+1)

trie = dict()
for _ in range(int(input())):
    depth, *words = input().split()
    insert(words)
    
sout(trie)