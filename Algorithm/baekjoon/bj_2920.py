a = list(map(int,input().split()))
b = a[:]
c = a[:]
b.sort()
c.sort(reverse=True)

if a == b :
    print("ascending")
elif a == c :
    print("descending")
else : 
    print("mixed")