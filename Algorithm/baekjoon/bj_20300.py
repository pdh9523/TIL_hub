N = int(input())
arr = sorted([ *map(int,input().split()) ])
if N % 2 == 1 :
    ans = arr.pop()
ans = 0

while arr :
    tmp = arr.pop()+arr.pop(0)

    ans = max(tmp,ans)
print(ans)