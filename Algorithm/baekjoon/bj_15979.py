def gcd(a,b):
    if not a: return b
    if not b: return a
    return gcd(b, a%b)

N,M = map(lambda x: abs(int(x)),input().split())
print(min(gcd(N,M),2))

