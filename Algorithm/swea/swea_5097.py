from collections import deque

t = int(input())

for i in range(t) :
    size, rotation = map(int, input().split())
    q = deque(map(int, input().split()))    # 큐도 맵을 받네요
    for _ in range(rotation) :  
        q.append(q.popleft())
    print(f"#{i+1} {q[0]}")     # 인덱싱도 가능