from math import pi

a,b,c = map(int,input().split())
if a>b: a,b=b,a
if a==b : exit(print(-1))

print(((2*a*c**2/(b-a))+c**2 +b**2 -a**2)*pi)