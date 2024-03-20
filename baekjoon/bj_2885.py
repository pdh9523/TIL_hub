t = int(input())
cnt = 0
for i in range(t):          # 올라갔다가
    if 2**i >= t :
        choco = 2**i
        idx = i
        break

for j in range(idx,-1,-1):  # 내려갔다가
    if 2**j <= t:
        t -= 2**j
        cnt = idx-j

    if not t :              # 0이면 탈출    
        break

print(choco,cnt)