N = int(input())
arr = input()

i,cnt = 0,0

while i < N :
    # 세자리씩 무조건 끊으려고 하면서, 앞자리가 0이면 우선 앞자리 한칸 앞으로 당기기
    if arr[i] == '0':
        i -=1
        # 카운트를 더하진 않음
        continue
    # 641일 이하면 인덱스 +3 해주기 (인덱스 범위가 벗어나는 경우에도 슬라이싱이라 인덱스 에러가 발생하지 않음)
    elif int(arr[i:i+3]) <= 641 : 
        i += 3
    # 641일 이상이면 +2 
    else :  
        i += 2

    cnt += 1

print(cnt)
