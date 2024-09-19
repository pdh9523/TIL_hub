import sys; input = sys.stdin.readline


class Trie:
    def __init__(self):
        self.root = dict()
    
    def insert(self, word):
        now = self.root

        for char in word:
            now[char] = now.setdefault(char, dict())
            now = now[char]
        now[0] = now.get(0, 0)+1

    def search(self, word):
        now = self.root
        ans = ""
        for char in word:
            ans += char
            if char not in now: return ans
            now = now[char]
        if 0 in now:
            ans += str(now[0]+1)
        return ans


trie = Trie()
for _ in range(int(input())):
    word = input().strip()
    print(trie.search(word))
    trie.insert(word)
