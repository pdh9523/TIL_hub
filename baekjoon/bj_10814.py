a= int(input())
test_dict = {}

for _ in range(a) :
    b,c = input().split()
    b= int(b)
    if b not in test_dict :
        test_dict[b] = [c]
    else :
        test_dict[b].append(c)

for i in range(201) :
    if i in test_dict : 
        for j in range(len(test_dict[i])) :
            print(f"{i} {test_dict[i][j]}") 