N = int(input())
A,B = map(int,input().split())
dough = int(input())

toppings = sorted([int(input()) for _ in range(N)], reverse=True)

ans = dough
cnt = A

for topping in toppings:
    # 토핑을 올려서 얻어지는 1원당 열량이 더 크면 토핑 올리기
    if (ans + topping) / (cnt+B) > ans / cnt:
        ans += topping
        cnt += B

print(ans//cnt)