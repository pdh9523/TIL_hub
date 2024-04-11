a,b = map(int,input().split())

basket = []

for i in range(a) :
    basket.append(int(input()))

count = 0
while len(basket) > 0 :
    if b >= basket[-1] :
        count += (b // basket[-1])
        b %= basket[-1]
    else : 
        basket.pop()
print(count)