_,a=open(0)
print(int("".join(sorted(a.split(),key=lambda x:x*9)[::-1])))