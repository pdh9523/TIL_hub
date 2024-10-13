import sys; input = sys.stdin.readline


def bisearch(array, r):
    left, right = 0, N
    while right > left:
        mid = (left + right) // 2
        if array[mid] <= r**2:
            left = mid + 1
        else:
            right = mid
    return left
    

def cal(ax,ay, dx,dy):
    return (ax-dx)**2 + (ay-dy)**2

cnt = 0
while N:=int(input()):
    cnt += 1
    arr,brr = [],[]
    data = [[*map(int,input().split())] for _ in range(N)]

    ax,ay,bx,by,q = map(int,input().split())

    for dx,dy in data:
        arr.append(cal(ax,ay, dx,dy))
        brr.append(cal(bx,by, dx,dy))
    
    arr.sort()
    brr.sort()

    print(f"Case {cnt}:")
    for _ in range(q):
        r1,r2 = map(int,input().split())
        ans = N - bisearch(arr, r1) - bisearch(brr, r2)
        print(ans if ans >0 else 0)