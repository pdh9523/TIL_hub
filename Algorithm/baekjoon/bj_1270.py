from collections import Counter
import sys;input = sys.stdin.readline


for _ in range(int(input())):
    N,*arr = map(int,input().split())
    arr = Counter(arr)
    
    ans,tmp = 0,0
    for i in arr:
        if arr[i] > tmp:
            ans = i
            tmp = arr[i]

    print(ans if arr[ans]>N/2 else "SYJKGW")