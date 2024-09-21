def f(n):
 if n in a: return a[n]
 a[n]=f(n//P)+f(n//Q)
 return a[n]
a = {0:1}
N,P,Q = map(int,input().split())
print(f(N))