a=t=0
for e,s in sorted([[*map(int,input().split())][::-1] for _ in[0]*int(input())]):
 if t<=s:t=e;a+=1
print(a)