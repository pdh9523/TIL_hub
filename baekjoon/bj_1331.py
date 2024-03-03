check = True                                            
alpha,num = {}, {}                                      # alpha : 알파벳 담을 딕셔너리, num : 숫자를 담을 딕셔너리
temp, tmp = list(input())                               # temp와 tmp :  A3 을 하나씩 담을 수 있다.
start_alpha, start_num = temp, tmp                      # 첫 시작값은 담아준다 (마지막 값에서 돌아올 수 있어야함)
alpha[temp], num[tmp] = 1, 1                            # 딕셔너리에 각 키값을 올려줌

for _ in range(35):                                     # 초기 설정에 하나 쓰고 나머지 35개
    alphabet,number = list(input())                     # alphabet - temp // number - tmp 서로 비교

    a = abs(ord(alphabet) - ord(temp))                  # a : 알파벳 간 차이
    n = abs(int(tmp) - int(number))                     # n : 숫자 간 차이
    if not 1<=a<=2 or not 1<=n<=2 or a+n != 3:          # 둘의 차이가 정상이 아니다 (알파벳의 이동이나 숫자의 이동이 1,2칸 내에서 이루어지지 않았거나, 총 3칸 이상 이동했거나)
        check = False                                   # check를 돌려 이후의 if문을 꺼버림
    
    alpha[alphabet] = alpha.get(alphabet, 0) + 1        # 딕셔너리에 각 키값을 올려줌
    num[number] = num.get(number, 0) + 1

    temp, tmp = alphabet, number                        # temp와 tmp에 alphabet과 number를 다시 담아서 번갈아 비교

if check :                                              # 일단 나이트가 35번 동안 무사히 돌았으면
    for v in alpha.values():                            # 1) 알파벳이 각각 6번씩 나왔는가?
        if v != 6:                                      
            print("Invalid")
            break
    else :
        for v in num.values() :                         # 2) 숫자가 각각 6번씩 나왔는가?
            if v != 6 :
                print("Invalid")
                break
        else :                                          # 3) 마지막 값에서 시작 위치로 돌아갈 수 있는가?
            if abs(ord(start_alpha) - ord(alphabet))+abs(int(start_num)-int(number))==3:

                print("Valid")

            else :
                print("Invalid")
else :                                                  # 4) check가 False가 된 경우(중간에 이미 끝난 경우) 
    print("Invalid")