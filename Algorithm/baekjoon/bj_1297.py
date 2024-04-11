import math
d,h,w = map(int,input().split())
a = d / math.sqrt(h**2 + w**2)
h = int(h*a)
w = int(w*a)
print(h,w)