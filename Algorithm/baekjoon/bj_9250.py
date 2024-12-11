# '''
# 문자열 집합 판별

# 아호 코라식

# 딕셔너리로 만든 트라이 구조로 아호 코라식도 날먹할 수 있지 않을까? 하는 생각에 온몸 비틀기를 해봤지만 안된다.
# 단순히 0을 문자열 마지막으로 두는 정도는 괜찮은데, 실패 링크를 같이 넣어서 판별하는건 쉽지 않다.

# 일단 간단한 방법이 있나 더 찾아보고, 할 수 있으면 간단한 방법으로 풀고 싶음
# 클래스로 구현하는게 썩 마음에 들지는 않음

# * 아호 코라식? KMP + 트라이다.
# '''
# import sys; input = lambda: sys.stdin.readline().strip()
# from collections import deque


# class Node:
#     def __init__(self,key=""):
#         self.key = key
#         self.children = dict()
#         self.fail = None
#         self.is_end = False


# class AhoCorasick:
    
#     def __init__(self, patterns):
#         self.root = Node()
#         for pattern in patterns:
#             self.insert(pattern)
#         self.connect()
    
#     def insert(self, pattern):
#         now = self.root

#         for char in pattern:
#             now = now.children.setdefault(char, Node(char))
#         now.is_end = True
    
#     def connect(self):
#         q = deque([self.root])

#         while q:
#             now = q.popleft()
#             for char in now.children:
#                 nxt = now.children[char]

#                 if now == self.root:
#                     nxt.fail = self.root
                
#                 else:
#                     dst = now.fail
#                     while dst != self.root and char not in dst.children:
#                         dst = dst.fail
                    
#                     if char in dst.children:
#                         dst = dst.children[char]
#                     nxt.fail = dst
                
#                 if nxt.fail.is_end:
#                     nxt.is_end = True
#                 q.append(nxt)
    
#     def search(self, word):
#         now = self.root

#         for char in word:
#             while now != self.root and char not in now.children:
#                 now = now.fail
#             if char in now.children:
#                 now = now.children[char]
#             if now.is_end:
#                 return True
#         return False

# ac = AhoCorasick([input() for _ in range(int(input()))])

# words = [input() for _ in range(int(input()))]
# for word in words:
#     print("YES" if ac.search(word) else "NO")


######### 찾은 풀이
import sys
from collections import deque

# 입력을 빠르게 받기 위한 설정
# `sys.stdin.readline()`은 입력 속도를 개선하는 데 사용되며, `strip()`은 입력의 공백 제거
input = lambda: sys.stdin.readline().strip()

# 트라이와 실패 링크를 구현하기 위한 루트 딕셔너리
trie = dict()

# 문자열 종료를 나타내는 키: '0'은 현재 노드가 패턴의 끝임을 의미
# 실패 링크를 나타내는 키: '1'은 실패했을 때 이동할 노드를 가리킴

# 트라이에 단어를 삽입하는 함수
def insert(word):
    now = trie  # 현재 노드를 루트로 설정
    for char in word:
        # 현재 노드에서 문자를 키로 가지는 딕셔너리를 생성(또는 이동)
        now = now.setdefault(char, dict())
    # 단어의 마지막 노드에 문자열 종료 표시
    now[0] = True

# 실패 링크를 생성하는 함수
def connect():
    # BFS를 사용하기 위해 큐를 초기화하고 루트 노드를 추가
    q = deque([trie])
    while q:
        now = q.popleft()  # 현재 처리 중인 노드
        for char in now:  # 현재 노드의 모든 자식 노드에 대해 처리
            # 실패 링크와 문자열 종료 표시는 건너뜀
            if char == 0 or char == 1:
                continue

            nxt = now[char]  # 자식 노드
            if now is trie:  # 현재 노드가 루트 노드인 경우
                nxt[1] = trie  # 자식 노드의 실패 링크를 루트로 설정

            else:             # 현재 노드가 루트 노드가 아닌 경우
                dst = now[1]  # 실패 링크를 따라감
                # 실패 링크를 계속 따라가면서 현재 문자가 없는 노드까지 이동
                while dst is not trie and char not in dst:
                    dst = dst[1]
                # 실패 링크에 문자가 존재하면 해당 노드를 설정
                if char in dst:
                    dst = dst[char]
            nxt[1] = dst  # 실패 링크 설정

            # 실패 링크가 문자열 종료를 포함하면 현재 노드도 문자열 종료로 표시
            if 0 in nxt[1]:
                nxt[0] = True

            # BFS를 위해 큐에 자식 노드 추가
            q.append(nxt)

# 문자열이 패턴에 포함되는지 확인하는 함수
def search(word):
    now = trie  # 현재 노드를 루트로 설정
    for char in word:
        # 실패 링크를 따라가면서 현재 문자가 존재하지 않는 노드를 건너뜀
        while now is not trie and char not in now:
            now = now[1]
        # 현재 노드에 문자가 존재하면 해당 자식 노드로 이동
        if char in now:
            now = now[char]
        # 현재 노드가 문자열 종료를 포함하면 패턴이 일치함
        if 0 in now:
            return True
    # 모든 문자에 대해 탐색했지만 패턴이 일치하지 않음
    return False

# 패턴 입력
patterns = [input() for _ in range(int(input()))]
# 각 패턴을 트라이에 삽입
for pattern in patterns:
    insert(pattern)

# 실패 링크 생성
connect()

# 검색할 문자열 입력
words = [input() for _ in range(int(input()))]
# 각 문자열에 대해 검색 수행
for word in words:
    # 검색 결과에 따라 "YES" 또는 "NO" 출력
    print("YES" if search(word) else "NO")