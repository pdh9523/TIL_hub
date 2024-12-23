'''
아스키 거리

아호 코라식

아호 코라식을 하면서, 스위핑처럼 처리를 하는거인줄 알았는데
그게 아니고 visit 처리 해야함

그리고, 아호 코라식 패턴에 5000*5000 을 넣기에는 너무 많아서,
아호 코라식을 끊어서 배치처리 하는 테크닉도 있다. 더라
'''

import sys; input = lambda: sys.stdin.readline().strip()
from collections import deque


class Node:
    def __init__(self):
        self.children = dict()
        self.fail = None
        self.end = 0


class AhoCorasick:
    def __init__(self):
        self.root = Node()
  
    def insert(self, pattern):
        now = self.root
        for char in pattern:
            now = now.children.setdefault(char, Node())

        now.end = len(pattern)
  
    def connect(self) :
        q = deque([self.root])
        while q :
            now = q.popleft()
            for char, nxt in now.children.items():
                if now == self.root:
                    nxt.fail = self.root
                else :
                    dst = now.fail
                    while dst != self.root and char not in dst.children:
                        dst = dst.fail

                    if char in dst.children:
                        dst = dst.children[char]

                    nxt.fail = dst
        
                    nxt.end = max(nxt.fail.end, nxt.end)
                
                q.append(nxt)
    
  
    def query(self, word) :
        now = self.root
        for i, c in enumerate(word) :
            while now != self.root and c not in now.children :
                now = now.fail
            if c in now.children : now = now.children[c]

            if now.end :
                start = i - now.end + 1
                visit[start] = max(visit[start], now.end) #더 긴 타일이 있다면 업데이트한다.


N = int(input())
word = input()

M = int(input())
P = [input() for _ in range(M)]
visit = [0] * N #i번째 위치에서 길이 visit[i]의 타일을 교체할 수 있다.

aho = AhoCorasick()
for i, s in enumerate(P):
    if i%100 == 0:
        aho.connect()
        aho.query(word)
        aho = AhoCorasick()

    aho.insert(s)

aho.connect()
aho.query(word)

left = 0
ans = [False] * N
for i, v in enumerate(visit): #순회하면서 교체할 수 있는 타일을 교체한 것으로 표시
    left = max(left, v)
    if left:
        ans[i] = True
    left -= 1
print(ans.count(False))