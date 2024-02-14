# from itertools import permutations

# t = int(input())

# for tc in range(t) :
#     size = int(input())
#     test_list = [list(map(int,input().split())) for _ in range(size)]
#     size_pmt = list(permutations(list(range(size)), size))
#     min_value = 100
#     for i in range(len(size_pmt)) :
#         output = 0
#         for j in range(size) :
#             output += test_list[j][size_pmt[i][j]]
#             if output > min_value :
#                 break
#         if min_value > output :
#             min_value = output
#     print(f'#{tc+1} {min_value}')


def permute(i, k, output) :                                             # runtime 떠서 포기함
    global min_v                                                        # 온라인 강사님 따라쳤습니다.
    if i == k :
        if min_v > output :
            min_v = output
    elif output >= min_v :
        return
    else :
        for j in range(i,k) :
            arr[i], arr[j] = arr[j], arr[i]
            permute(i+1, k, output+test_list[i][arr[i]])
            arr[i], arr[j] = arr[j], arr[i]


t = int(input())
for idx in range(t) :
    N = int(input())
    test_list = [list(map(int,input().split())) for _ in range(N)]
    arr = list(range(N))
    min_value = 100
    permute(0,N,0)
    print(f"#{idx+1} {min_v}")