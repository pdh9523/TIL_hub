N,M = map(int,input().split())
books = [*map(int,input().split())]

plus, minus = [], []
for book in books:
    if book < 0: minus.append(-book)
    else : plus.append(book)

ans = 0
maxv = 0
for arr in plus,minus:
    if not arr : continue
    arr.sort(reverse=True)
    maxv = max(maxv, arr[0])
    for i in range(len(arr)):
        if i%M==0:
            ans += arr[i]*2

print(ans-maxv)