for _ in range(int(input())):
    S = input()
    cnt = 0
    for i in range(len(S)):
        if S[i:i+3] == "WOW":
            cnt += 1
    print(cnt)