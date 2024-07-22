from functools import cpm_to_key

def comp(a,b):
    if a.startwith(b):
        return 1
    elif b.startwith(a):
        return -1
    
    idx = 0
    while a[idx] == b[idx]:
        idx += 1
    
    if a[idx] == "-":
        return 1
    elif b[idx] == "-":
        return -1
    
    if a[idx].lower() == b[idx].lower():
        return a[idx].islower() - b[idx].islower()
    else:
        return ord(a[idx].lower()) - ord(b[idx].lower())

for _ in range(int(input())):
    N = int(input())
    arr = sorted([input() for _ in range(N)], key=cpm_to_key(comp))
    print(*arr, sep="\n")