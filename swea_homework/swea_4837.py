test_list = [x for x in range(1,13)] 
subset = [[]]
for element in test_list :
    size = len(subset)
    for i in range(size) :
        subset.append(subset[i]+[element])
# 부분집합 만드는 것 외우기
        
t = int(input())

for i in range(t) :
    N,K = map(int,input().split())
    count = 0
    for sub in subset :
        if len(sub) == N and sum(sub) == K :
            count += 1
    print(f"#{i+1} {count}")