from collections import deque

N,K = map(int,input().split())

belt = list(map(int,input().split()))

upper = deque(belt[:N])
under = deque(belt[N:])

