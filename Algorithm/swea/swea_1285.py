test_case = int(input()) #테스트 케이스

def absint(n) :
    return abs(int(n))

for i in range(test_case) :
    test_number = int(input()) #인원수
    test_range = list(map(absint,input().split()))
    rem = {}
    for j in test_range :
        if j in rem :
            rem[j] +=1
        else :
            rem[j] = 1
    for key in rem :
        key_rem=[]
        key_rem.append(key)
    target = min(test_range)
    print(f"#{i+1} {target} {rem[target]}")