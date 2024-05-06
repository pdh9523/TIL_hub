from collections import deque

N = int(input())

text_list = []
for _ in range(N):
    text_list.append(deque(input().split()))

target = deque(input().split())
ans = "Possible"

while target :
    t = target.popleft() 

    for i in range(N) :

        if text_list[i] and text_list[i][0] == t :
            text_list[i].popleft()
            break
    else :
        ans = "Impossible"
        break

if any(text_list) :
    ans = "Impossible"

print(ans)