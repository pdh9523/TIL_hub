test_list = [x for x in range(1,13)] 
subset = [[]] #공집합 넣어두고 시작
for element in test_list :
    size = len(subset) # 시행마다 길이가 달라지고, 그 만큼 새로운 원소를 다 투입함 (1, 1+1, 1+1+2, 1+1+2+4, 1+1+2+4+8, ...)
    for idx in range(size) :
        subset.append(subset[idx]+[element]) # 공집합에서 시작해서, 만들어진 각 값에 대해 값을 더해 새로운 리스트를 생성
        # [] 이면 []+1 해서 [1] //  [], [1] 이면 []+2, [1]+2 해서 [2],[1,2] -> [], [1], [2], [1,2]
# 부분집합 만드는 것 외우기
        
t = int(input())

for i in range(t) :
    N,K = map(int,input().split())
    count = 0
    for sub in subset :
        if len(sub) == N and sum(sub) == K :
            count += 1
    print(f"#{i+1} {count}")