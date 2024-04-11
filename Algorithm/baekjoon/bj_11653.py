a = int(input()) # 정수 입력

div = 2 # 인수 설정
while a > 1 : # 마지막으로 1이 반환될 때 반복 종료
    if a % div == 0 :
        a = a / div
        print(div) # 나눠지면 바로바로 출력
        div = 2 # 인수 초기화
    else :
        div += 1 # 안나눠지면 값을 올려서 반복