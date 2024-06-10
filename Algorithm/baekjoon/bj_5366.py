import sys

input = sys.stdin.readline

obj = dict()
while True :
    txt = input().strip()
    if txt == "0":
        break
    
    obj[txt] = obj.get(txt,0)+1
ans = 0 
for k,v in obj.items():
    print(f"{k}: {v}")
    ans += v
print("Grand Total:",ans)