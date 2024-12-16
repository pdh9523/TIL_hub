arr = list(range(int(input())+1))
brr = sorted([[*map(int,input().split())] for _ in range(int(input()))], key=lambda x:(x[0],-x[1]))

for a,b in brr:
    for i in range(a,b+1):
        arr[i]=arr[a]
print(len(set(arr[1:])))
