B,C,D = map(int,input().split())

burger = sorted([*map(int,input().split())])
side = sorted([*map(int,input().split())])
drink = sorted([*map(int,input().split())])
print(sum(burger)+sum(side)+sum(drink))
ans = 0

while burger and side and drink:
    if burger and side and drink :
        ans += int((burger.pop() + side.pop() + drink.pop()) * 0.9)
ans += sum(burger) + sum(side) + sum(drink)

print(ans)