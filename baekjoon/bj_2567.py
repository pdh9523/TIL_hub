space = [[0 for _ in range(101)] for _ in range(101)] # 인덱스 에러 방지를 위해 한칸 더 큰 리스트를 준비 (왼쪽은 0부터 시작하니까 상관없음)

t = int(input())
count = 0 # 결과 담을 변수
for _ in range(t) :
    x,y = map(int,input().split())
    #색종이 칠하기
    for i in range(x,x+10) :
        for j in range(y,y+10) :
            space[i][j] = 1     

#겉에 있는 1의 값들을 모두 더한다.
for i in range(100) :
    for j in range(100) :
        if space[i][j] == 1 and space[i][j+1] == 0 :
            count += 1
        if space[j][i] == 1 and space[j+1][i] == 0 :
            count += 1
        if space[i][j] == 1 and space[i][j-1] == 0 :
            count += 1
        if space[j][i] == 1 and space[j-1][i] == 0 :
            count += 1
# 결과 출력
print(count)