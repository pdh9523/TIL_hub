a,b = map(int,input().split()) # 초기 설정
basket = {} # 바구니는 딕셔너리로
for i in range(a+1) : # 바구니 1개 더 만듬 (0을 안쓰면 인덱스 구분하기 쉬울 것 같아서)
    basket[i] = i # 딕셔너리 인덱스에 같은 숫자 담음

for j in range(b) : # 공 바꾸기
    c,d = map(int,input().split())
    basket[c], basket[d] = basket[d], basket[c]

for i in range(1,a+1) : # basket[0] = 0 이니까 빼고 출력
    print(basket[i], end=" ")