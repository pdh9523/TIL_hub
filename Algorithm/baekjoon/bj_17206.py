N=int(input())
arr=[*map(int,input().split())]
ans = dict()

for num in arr: 
    tmp = 0
    for i in range(num+1):
        if i%3==0 or i%7==0 :
            tmp += i
    ans[num] = tmp

print(*ans.values(), sep="\n")