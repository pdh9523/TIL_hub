# 입력 단계
N = int(input())
buildings = list(map(int,input().split()))

# 정답(최대값) 갱신
ans = 0

# 전체를 순회하면서 
for i in range(N):
    
    cnt = 0
    # 순회하고 있는 빌딩에서 왼쪽으로는 왼쪽으로 멀어지면서, 오른쪽으로는 오른쪽으로 멀어지면서
    # 건물을 기준으로 ratio가 커지면 cnt += 1 하는 방식
    # ratio : (상대빌딩 - 내 빌딩) / 거리

    #왼쪽 (tmp 초기화)
    tmp = -float('inf')
    for j in range(i-1,-1,-1):
        width = abs(i-j)
        height = buildings[j] - buildings[i]
        ratio = height/width
        # ratio가 tmp보다 크면 cnt +=1 하고 갱신
        if ratio > tmp :
            cnt += 1
            tmp = ratio

    # 오른쪽 (tmp 초기화)
    tmp = -float('inf')
    for j in range(i+1,N):
        width = abs(i-j)
        height = buildings[j] - buildings[i]
        ratio = height/width
        if ratio > tmp :
            cnt += 1
            tmp = ratio

    # 한 건물에 대한 순회가 마치면 최대값 갱신
    ans = max(ans,cnt)
print(ans)