# 정렬된 값과 같은 경우(-1,-2 교환)
# 그렇지 않은 경우 (가장 큰값을 앞으로, 그다음 큰 값을 2번째로,, 반복)

t = int(input())

num, count = input().split()
count= int(count)
num = list(map(int,list(num)))

while count :
    if num[0] != max(num) :
        