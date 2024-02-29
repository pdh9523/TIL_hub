check = True
alpha,num = {}, {}
temp, tmp = list(input())
start_alpha, start_num = temp, tmp 
alpha[temp], num[tmp] = 1, 1

for _ in range(35):
    alphabet,number = list(input())

    a = abs(ord(alphabet) - ord(temp))
    n = abs(int(tmp) - int(number))
    if not 1<=a<=2 or not 1<=n<=2 or a+n != 3:
        check = False
    
    alpha[alphabet] = alpha.get(alphabet, 0) + 1
    num[number] = num.get(number, 0) + 1

    temp, tmp = alphabet, number

if check :
    for v in alpha.values():
        if v != 6:
            print("Invalid")
            break
    else :
        for v in num.values() :
            if v != 6 :
                print("Invalid")
                break
        else :
            if abs(ord(start_alpha) - ord(alphabet))+abs(int(start_num)-int(number))==3:

                print("Valid")

            else :
                print("Invalid")
else :
    print("Invalid")