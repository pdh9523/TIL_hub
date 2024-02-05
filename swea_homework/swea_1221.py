number_dict = {"ZRO" : 0,
               "ONE" : 1,
               "TWO" : 2,
               "THR" : 3,
               "FOR" : 4,
               "FIV" : 5,
               "SIX" : 6,
               "SVN" : 7,
               "EGT" : 8,
               "NIN" : 9}

t = int(input())
for i in range(t):
    _,__ = input().split() # 사실 쓸 필요가 있을까 싶었습니다.
    test_list = input().split() # 정렬해야할 변수를 리스트에 담고
    test_list.sort(key=lambda x : number_dict[x]) # 정렬
    print(f"#{i+1}", *test_list) # 언패킹