N,r,c = map(int,input().split())    # r : 행 (세로) c : 열 (가로)
ans = 0 
while N != 0 :              # z 크기까지 
    N -= 1                  # 분할 

    target = 2**N           # 사분면 단위로 그었을 때, 기준이 되는 선분의 위치

    # 점이 각각 N분면에 있는 경우 값을 ans에 합하는 방식으로 위치를 계산. 
    if r >= target and c >= target :  # 4 사분면
        ans += target**2 *3
        r -= target
        c -= target

    elif r >= target and c < target : # 3 사분면
        ans += target**2 *2
        r -= target
        
    elif r < target and c >= target : # 2 사분면
        ans += target**2
        c -= target
        
print(ans)