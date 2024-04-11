case_pointer = 0
while True :
    a,b,c = map(int,input().split())
    if max(a,b,c) == 0 :
            break
    
    camping = (c // b)

    camping_day = (c//b)*a 

    rem = c - b*camping

    if rem > a :
        camping_day += a 
    else : 
        camping_day += rem
    case_pointer += 1
    print(f"Case {case_pointer}: {camping_day}")
