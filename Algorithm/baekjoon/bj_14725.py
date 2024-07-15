import sys

class Trie:
    def __init__(self):
        self.root = dict()
    

    def insert(self, foods):
        now = self.root
        for food in foods:
            now = now.setdefault(food, dict())


    def dfs(self, now, level=0):
        for nxt in sorted(now):
            print("--"*level+nxt)
            self.dfs(now[nxt], level+1)

input = sys.stdin.readline
trie = Trie()
for _ in range(int(input())):
    n,*foods = input().split()
    trie.insert(foods)
trie.dfs(trie.root)