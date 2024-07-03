def convert(n,ans=""):
    if n == 0: return 0

    while n !=0:
        n,res = divmod(n,3)
        if res == 2: n += 1
        ans += str(res)
    return ans[::-1].replace("2","-")

for _ in range(int(input())):
    print(convert(int(input())))