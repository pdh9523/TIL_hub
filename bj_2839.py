a = int(input())


big_5 = a // 5 +1
big_3 = 0


while a != big_5*5 + big_3*3 : 
    if a in [1,2,4,7] :
        print(-1)
        break
    if big_5*5 + big_3*3 > a :
        big_5 -= 1
    if big_5*5 + big_3*3 < a :    
        big_3 += 1
    if big_5*5 + big_3*3 == a :
        print(big_3+big_5)
        break