a,b = map(int,input().split())
pass_dict = {}
for i in range(a) :
    site, password = input().split(" ")
    pass_dict[site] = password

for j in range(b) :
    target = input()
    print(pass_dict[target])