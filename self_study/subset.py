arr = [x for x in range(4)] # 0 1 2 3
n = len(arr)
bitset = [] # 모든 부분집합을 담을 리스트
for i in range(1<<n) : # i = 0, 1, 2, 3, 4, 5, ... 15 (1<<n == 2**n)
    test_list = [] # 원소 담을 리스트
    for j in range(n) : # j = 0, 1, 2, 3
        if i & (1<<j) : # i는 10진수, 1>>j는 2,4,8,16 (이진변환) 
        # i가 1, 2, 3, 4 째 자리 중 하나에 들어가 있나요?
        # i를 이진변환해 1011이면 if문에서 j == 3, 1, 0 일때 걸려서 세개를 추출
            test_list.append(arr[j]) # 들어가 있으면 리스트에 담기 
    if len(test_list) >= 2 : # 이 과정에서 길이를 제한 가능
        bitset.append(test_list) # 부분 집합 리스트를 큰 리스트에 담기


print(bitset) # 모든 부분 집합이 들어있는 큰 리스트 출력

# 비트연산이 싫어요
test_list = [x for x in range(4)] # 0 1 2 3
subset = [ [] ] # 공집합 넣어두고 시작
for element in test_list :
    size = len(subset) # 시행마다 길이가 달라지고, 그 만큼 새로운 원소를 다 투입함 (1, 1+1, 1+1+2, 1+1+2+4)
    for i in range(size) :
        subset.append(subset[i]+[element]) # 공집합에서 시작해서, 만들어진 각 값에 대해 값을 더해 새로운 리스트를 생성
        # [] 이면 []+1 해서 [1] //  [], [1] 이면 []+2, [1]+2 해서 [2],[1,2] -> [], [1], [2], [1,2]
print(subset)