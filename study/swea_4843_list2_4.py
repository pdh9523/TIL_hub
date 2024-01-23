t = int(input()) #테스트 케이스

for test in range(t) :
    length = int(input()) # 길이
    arr = list(map(int,input().split())) # 리스트 입력
    arr.sort() # 정렬 
    rot = length//2 # 반복하면서 담을거니까 반갈죽
    lower_arr=arr[:rot] # 아래쪽 리스트 만들기
    upper_arr=arr[rot:] # 위쪽 리스트 만들기
    upper_arr.sort(reverse=True) # 위쪽 리스트 내림차순 정렬

    result = []
    for i in range(5) : # 5+5 10개 남기기
        result.append(upper_arr[i]) # 큰 수 먼저
        result.append(lower_arr[i]) # 그 뒤 작은 수
    print(f"#{test+1}",*result) # 출력