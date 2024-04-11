N = int(input())

dots = [list(map(int,input().split())) for _ in range(N)]

output1 = 0 
output2 = 0

for i in range(N):
    output1 += dots[i-1][0] * dots[i][1]
    output2 += dots[i][0] * dots[i-1][1]

print(round(abs(output1-output2)/2,2))
# 이건 수학 공식이니까..
