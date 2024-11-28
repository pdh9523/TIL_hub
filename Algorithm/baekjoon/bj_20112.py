def check():
    for i in range(N):
        for j in range(N):
            if arr[i][j] != arr[j][i]:
                return False
    return True


N = int(input())
arr = [list(input()) for _ in range(N)]
print("YES" if check() else "NO")