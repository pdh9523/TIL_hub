t, test_case = map(int,input().split())

test_list = list(map(int,input().split()))
test_dict = {}
for idx in range(0,len(test_list),2) :
    if test_list[idx] not in test_dict :
        test_dict[test_list[idx]] = [test_list[idx+1]]
    else :
        test_dict[test_list[idx]].append(test_list[idx+1])
# 리스트로 기차놀이를 해야하나?
i = 0
while True :
    for j in test_dict[i] : # 에서 2개의 값을 전수조사를 할 수 있나?
        if 99 in test_dict[j] :
            print(1)
    else:
        i = j

print(0)