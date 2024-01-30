a,b = map(int,input().split())

a = set(map(int,input().split()))
b = set(map(int,input().split()))

if a.issubset(b) :
    print(0)
else : 
    a = a - b
    a = list(a)
    a.sort()
    print(len(a))
    print(*a)