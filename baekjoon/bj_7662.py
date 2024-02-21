from collections import deque

t = int(input())

for _ in range(t):
    k = int(input())
    max_value = -1 * float("inf")
    min_value = float("inf")
    q = deque()
    for _ in range(k):
        order,value = input().split()
        value = int(value)
        if order == "I":
            q.append(value)
            if value > max_value :
                max_value = value
            elif value < min_value :
                min_value = value
        else :
            if value == -1 :

### 힙 연산 배우고 풀 것