def collatz(num, visit):
    visit.append(num)

    if num == 1:
        return visit
    
    nxt = num*3 +1 if num%2 else num // 2
    collatz(nxt, visit)


def collatz_comp(num):
    global ans, cnt
    if not ans and num in arr:
        ans = num
        return
    if num == 1:
        return
    cnt += 1
    nxt = num*3 +1 if num%2 else num // 2
    collatz_comp(nxt)


for _ in range(100000000):
    ans = 0
    N,M = map(int,input().split())
    if not N and not M: break
    arr = []
    collatz(N,arr)
    cnt = 0
    collatz_comp(M)
    print(f"{N} needs {len(arr[:arr.index(ans)])} steps, {M} needs {cnt} steps, they meet at {ans}")