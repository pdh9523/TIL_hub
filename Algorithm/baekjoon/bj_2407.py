from fractions import Fraction

def fac(n):
    if n == 0 :
        return 1
    return n * fac(n-1)

def comb(n,m):
    return Fraction(fac(n), (fac(m)*fac(n-m)))


n,m=map(int,input().split())
print(comb(n,m))