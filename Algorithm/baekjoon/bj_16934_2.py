import sys; input = sys.stdin.readline


def insert(word):
    now = trie
    for char in word:
        now = now.setdefault(char, dict())
    now["cnt"] = now.get("cnt",0)+1

def search(word):
    now = trie
    result = ""
    for char in word:
        result += char
        if char not in now:
            return result
        now = now[char]
    if "cnt" in now:
        result += str(now["cnt"]+1)
    return result


trie = dict()
for _ in range(int(input())):
    word = input().strip()
    print(search(word))
    insert(word)
