a = int(input())
arr_a = list(map(int,input().split()))

b = int(input())
arr_b = list(map(int,input().split()))

dic = {}
for item in arr_a:
    dic[item] = dic.get(item, 0) + 1

for i in arr_b:
    print(dic.get(i,0), end=" ")