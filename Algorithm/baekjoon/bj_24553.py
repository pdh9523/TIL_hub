# 패리티..어쩌구를 쓸 수 있는가? 

# 회문 수 :
# 1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 22, 33, 44 ,55 ,66 ,77 ,88 ,99, 101, 111, 121, 131, ...
for _ in range(int(input())):print(int(input()[-1]=="0"))

#
for _ in range(int(input())):
    stone = int(input())
    if stone % 10 :
        print(1)
    else :
        print(0)