# 기준을 최소값에 두고 해싱

N = int(input())

arr = list(map(int,input().split()))

sorted_arr = sorted(arr)

dic,idx = {}, 0
for item in sorted(arr) :
    if item not in dic :
        dic[item] = idx
        idx += 1

for i in arr:
    print(dic[i], end=" ")