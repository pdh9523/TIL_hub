class Node():
    def __init__(self,data):
        self.data = data
        self.child = [None] * 26
        self.is_end = False

class Trie:
    
    def __init__(self):
        self.root = Node("")
    
    def insert(self,text):
        now = self.root

        for char in text:
            idx = ord(char)-ord('a')
            if now.child[idx] != None:
                now = now.child[idx]
            else:
                new = Node(char)
                now.child[idx] = new
                now = new
        now.is_end = True
    
    def dfs(self, now, level=0,text=""):
        for idx in range(26):
            if now.child[idx]:
                print(text)
                self.dfs(now.child[idx], level+1, text+chr(ord('a')+idx))
    
trie = Trie()
for _ in range(int(input())):
    N = int(input())
    text = input()
    trie.insert(text)

    trie.dfs(trie.root)