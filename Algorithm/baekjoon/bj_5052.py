import sys
input = sys.stdin.readline

class Node:
    def __init__(self,data):
        self.data = data
        self.child = [None]*10
        self.check = False

class Trie:
    def __init__(self):
        self.root = Node('')

    def insert(self,phone):
        tmp = self.root
        for i in phone:
            if tmp.child[i] != None:
                tmp = tmp.child[i]
            else:
                new = Node(i)
                tmp.child[i] = new
                tmp = new
        tmp.check = True

    def consistency(self, phone):
        tmp = self.root
        for i in range(len(phone)):
            if tmp.check:
                return False
            tmp = tmp.child[phone[i]]
        return True

for _ in range(int(input())):
    N = int(input())
    arr = []
    trie = Trie()

    for _ in range(N):
        phone = [*map(int,list(input().strip()))]
        trie.insert(phone)
        arr.append(phone)
    res = True

    for data in arr:
        res *= trie.consistency(data)
    
    print("YES" if res else "NO")