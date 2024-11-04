'''
다이어트, 투포인터
start와 end가 N만큼 차이나는 값을 찾으면 ans 에 넣고, 아니면 차이에 따라 조절한다.
'''
N = int(input())

start,end = 1,2 
ans = []
while start < end:
    if end**2 - start**2 == N:
        ans.append(end)
        end += 1
    elif end**2 - start**2 < N:
        end += 1
    else :
        start += 1

if ans:
    print(*ans, sep="\n")
else:
    print(-1)