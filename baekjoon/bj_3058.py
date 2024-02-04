t = int(input())

for _ in range(t) :
    test_list = list(map(int,input().split()))
    not_odd = []
    for ele in test_list :
        if ele % 2 == 0 :
            not_odd.append(ele)
    not_odd.sort()
    print(sum(not_odd), not_odd[0])