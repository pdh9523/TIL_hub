N = list(input())
M = list(input())

lenn,lenm=len(N),len(M)

n,m = 0,0

while n != lenn and m != lenm :
    if N[n] == M[m] :
        n,m = n+1, m+1
    