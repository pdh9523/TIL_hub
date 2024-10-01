N = int(input())
ballons = [*map(int,input().split())]
cnt = 0
height = [0]*1000001
for b in ballons:
    height[b-1]+=1
    if height[b]:
        height[b]-=1
    else:
        cnt+=1
print(cnt)