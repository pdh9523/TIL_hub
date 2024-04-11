S,T=list(input()),list(input())
while T!=S:
    if T.pop()=="B": T=T[::-1]
    if not T: exit(print(0))
print(1)