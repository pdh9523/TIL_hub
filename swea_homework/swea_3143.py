t = int(input())

for i in range(t) :
    a,b = input().split()

    print(f"#{i+1} {len(a)-(a.count(b)*(len(b)-1))}")