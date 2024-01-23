a = int(input())

target = 1000 - a #거스름돈
count = 0 #카운트


while target >= 500 : #500원 거슬러주면 거스름돈에서 500원 깎고 카운트 올림
    target -= 500
    count+=1
while target >= 100 :
    target -= 100
    count += 1
while target >= 50 :
    target -= 50 
    count +=1
while target >= 10 :
    target -= 10
    count += 1
while target >= 5 :
    target -= 5
    count += 1
while target >= 1 :
    target -= 1
    count += 1
print(count) # 차례로 내려오면서 비교