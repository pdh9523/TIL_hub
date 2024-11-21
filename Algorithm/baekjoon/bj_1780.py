import sys; input=sys.stdin.readline


def get_papers(num, i=0, j=0):
    now = arr[i][j]

    for ni in range(i, i+num):
        for nj in range(j, j+num):
            if arr[ni][nj] == now: continue

            nxt = num // 3

            for x in range(i, i+num, nxt):
                for y in range(j, j+num, nxt):
                    get_papers(nxt, x, y)
            return
        
    ans[now] += 1
    return


N = int(input())
arr = [[*map(int,input().split())] for _ in range(N)]

ans = [0]*3

get_papers(N)

print(ans[-1])
print(ans[0])
print(ans[1])