def arr_sum(idx=0,total=0):
    global ans

    if idx == size :
        if total < ans:
            ans = total
            return
    
    if total > ans :
        return

    for i in range(size):
        if i not in visit:
            visit.append(i)
            arr_sum(idx+1, total+arr[idx][i])
            visit.pop()


t = int(input())

for idx in range(t):
    size = int(input())
    arr = [list(map(int,input().split())) for _ in range(size)]
    ans = float("inf")
    visit = []

    arr_sum()
    print(ans)