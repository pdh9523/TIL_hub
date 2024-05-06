for _ in range(int(input())):
    N = int(input())
    arr = input().split()
    ans = ""
    for char in arr :
        if ans and ans[0] >= char :
            ans = char + ans
        else :
            ans = ans + char
    print(ans)