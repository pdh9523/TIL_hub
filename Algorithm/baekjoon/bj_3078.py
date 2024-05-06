import sys
from collections import deque

input = sys.stdin.readline


N,K = map(int, input().split())
len_num = dict()
cnt = 0

student = []

for i in range(N):
    student.append(len(input().strip()))
    # 슬라이딩 윈도우
    if i > K:
        len_num[student[i-K-1]]-=1
    
    cnt += len_num.setdefault(student[i],0)
    len_num[student[i]] += 1

print(cnt)