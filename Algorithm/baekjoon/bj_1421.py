N,C,W = map(int,input().split())

trees = [ int(input()) for _ in range(N) ]
ans = 0
M = max(trees)
# 나무를 자를 수 있는 각 단위를 i로 
for i in range(1,M+1):
    # 나누어 떨어지면 한번 기회는 빼주는걸로
    length = 0
    cnt = 0
    for tree in trees :
        check = 0
        tmp = tree//i
        if tree%i == 0 :
            check = 1
        # 한 나무를 그냥 안쓰는 경우도 있다.
        if i*tmp*W-(tmp-check)*C > 0 :
            length += tmp
            cnt += check
    ans = max(i*length*W-(length-cnt)*C, ans)

print(ans)
