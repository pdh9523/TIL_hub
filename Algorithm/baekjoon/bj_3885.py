# 값은 0부터 100까지
# 그럼 ..
while True:
    N,M = map(int,input().split())
    if N==M==0: break

    data = [0]*101

    for _ in range(N):
        data[int(input())] +=1

    diagram = []
    cnt,idx = 0,-1 
    while True:
        idx += 1
        if idx and idx % M == 0:
            diagram.append(cnt)
            cnt = 0 
        
        cnt += data[idx] 

        if idx == 100 :
            diagram.append(cnt)
            break
    while diagram[-1]==0:
        diagram.pop()

    length = len(diagram)

    ans = 0
    max_value = 0
    for value in diagram:
        length -=1
        ans += length*value
        max_value = max(max_value,value)
    print(ans/(len(diagram)-1)/max_value + 0.01)
