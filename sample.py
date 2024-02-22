t = input()
tt = list(map(int, list(t)))
if int(t) % 3 == 0 and "0" in t :
    tt.sort(reverse=True)
    print(*tt, sep="")
else :
    print(-1)