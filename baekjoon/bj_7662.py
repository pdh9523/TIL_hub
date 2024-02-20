from collections import deque

t = int(input())

for _ in range(t):
    k = int(input())
    max_value = -1 * float("inf")
    min_value = float("inf")
    for _ in range(k):
        q = deque()
