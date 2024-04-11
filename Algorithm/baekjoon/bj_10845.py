import sys

t = int(input())
q = []

for _ in range(t) :
    tc = sys.stdin.readline().strip("\n")
    if "push" in tc :
        _,v = tc.split()
        q.append(v)
    elif tc == "pop" :
        if q :
            print(q.pop(0))
        else :
            print(-1)
    elif tc == "size" :
        print(len(q))
    elif tc == "empty" :
        if len(q)==0 :
            print(1)
        else :
            print(0)
    elif tc == "front":
        if q :
            print(q[0])
        else :
            print(-1)
    elif tc == "back" :
        if q :
            print(q[-1])
        else :
            print(-1)