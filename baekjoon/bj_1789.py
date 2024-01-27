a = int(input())
n = 0

while n*(n+1) / 2 < a : 
    n+=1

print (int(n + (a - n * (n+1) / 2) // n ))