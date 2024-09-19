import sys; input = sys.stdin.readline


def check(target):
    cur = col_trie
    for i in range(len(target)):
        if 0 in cur and target[i:] in team:
            return True

        if not target[i] in cur:
            return False

        cur = cur[target[i]]


N,M = map(int,input().split())

col_trie = dict()
for _ in range(N):
    col = input().strip()
    cur = col_trie
    for i in col:
        cur = cur.setdefault(i, dict())
    cur[0] = True

team = set(input().strip() for _ in range(M))

for _ in range(int(input())):
    print("Yes" if check(input().strip()) else "No")