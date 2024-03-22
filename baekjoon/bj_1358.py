import math

X,H,X,Y,P = map(int,input().split())
# width를 제거하면 되는거아닙니까

radius = H/2

for _ in range(P):
    x,y = map(int,input().split())
    
    if 