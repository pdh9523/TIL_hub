data = []
for _ in range(3):
    a = input().split()
    if not a :
        a = input().split()
    data.append(a)
# data = [ input().split() for _ in range(3) ]    

ans = []
for i in range(1,13): # 1부터 12까지
    for w in -1,1 : 
        arr = [0]*13
        arr[i] = w
    
        for line in data:
            a=0
            b=0
            for x in range(4):
               a+=arr[int(line[x])]
               b+=arr[int(line[x+5])]

            if line[4] == "=":
                line[4] = "==" 
            if not eval(f"{a} {line[4]} {b}"):
               break
        else :
            if w == -1:
                ans.append(f"{i}-")
            else :
                ans.append(f"{i}+")

if len(ans)>1:
    print("indefinite")
elif len(ans)==0:
    print("impossible")
else :
    print(*ans)