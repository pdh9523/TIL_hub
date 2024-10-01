def cal():
    for i in sorted(real_pal):
        if i<N: continue
        for j in range(2,int(i**0.5)+1):
            if i%j==0:
                break
        else: print(i)


def is_pal(num):
    num_s = str(num)
    if num_s == num_s[::-1]:
        return True


pal = ["", "0","1","2","3","4","5","6","7","8","9"]
real_pal = {5,6,7,8,9}
def make_pal():
    for i in pal:
        if len(i) > 8: break
        for j in range(10):
            tmp = str(j)+i+str(j)
            pal.append(tmp)
            if N <= int(tmp) <= M:
                real_pal.add(int(tmp))


N,M = map(int,input().split())
make_pal()
cal()
print(-1)