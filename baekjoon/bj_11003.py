from collections import deque

N,L = map(int,input().split())

arr = list(map(int,input().split()))

q = deque()

for i in range(N) :
    
    while q and q[-1][0] > arr[i] :     # 뒤에 들어있는 값이 들어올 값보다 작으면 일단 다 제거
        q.pop()
    
    q.append((arr[i], i+1))             # 들어올 값 추가 (값, 인덱스 방식)

    if q[-1][1] - q[0][1] >= L:         # 들어온 값의 인덱스와 맨 앞의 인덱스가 L 만큼 차이날 경우 제거
        q.popleft()

    print(q[0][0], end=" ")             # Q의 가장 앞이 최소값이 되고, 그것의 값을 출력
    