N,M = map(int,input().split())
ans = 0
bed = 0
bal = 0
for _ in range(N):
    size, name = input().split()
    size = int(size)
    if name =="bedroom":
        bed += size
    if name == "balcony":
        bal += size / 2

    ans += size

print(ans)
print(bed)
print((ans-bal)*M)