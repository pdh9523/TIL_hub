t = int(input())

for i in range(t) :
    n = int(input())
    test_list = [[x for x in input().split()] for _ in range(n)]
    
    tilted_list = []
    for x in range(n) :
        rem = []
        for y in range(n-1,-1,-1) :
            rem.append(test_list[y][x])
        tilted_list.append(rem) 

    print(f"#{i+1}")
    for idx in range(n) :
        print("".join(tilted_list[idx]), "".join(test_list[n-idx-1][::-1]), "".join(tilted_list[n-idx-1][::-1]))
