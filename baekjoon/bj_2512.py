from sys import stdin

t =int(input())
test_list = list(map(int,stdin.readline().split()))
target = int(input())

budget = target // t 
count = 0
for number in test_list :
    if budget >= number :
        target -= number
    else : 
        count +=1
if count > 0 :
    if target//count > max(test_list) :
        print(max(test_list))
    else :
        print(target//count)
else :
    if budget > max(test_list) :
        print(max(test_list))
    else :
        print(budget)