N,C,W = map(int,input().split())
test_list = []
for _ in range(N) :
    test_list.append(int(input()))

# 1,2,100 같은게 들어가면 안자르는게 나음. 괜히 다 팔겠다고 1 단위로 자르면 자르는 비용이 더나감
# 1,5,10 정도되면 자르는 비용을 고려해야함
# 완전검색 ㄱ?
# sort해서 최소치부터 잘랐을 때 이득을 모두 계산
# 26 103 59 에서, 기준을 13으로 맞추네..아니
# 최대 공약수를 찾되, 몇 정도는 버려도 괜찮다고 생각해야되는데
test_list.sort()
result_list = []
for tree in test_list :
    result = 0 
    for others in test_list :
        result += ((others // tree)) * W * tree
        if others % tree != 0 :
            result -= (others//tree) * C
        else :
            result -= (others//tree) * (C-1)
        result_list.append(result)
