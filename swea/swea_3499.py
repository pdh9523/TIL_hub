import math

t = int(input())

for idx in range(t):
    size = int(input())
    card = input().split()
    re_size = math.ceil(size/2)     # 카드 나누는 기준

    card_left = card[:re_size]
    card_right = card[re_size:]


    print(f"#{idx+1}", end = " ")   # 인덱스

    for i in range(re_size):            # left가 많으니까 거기까지 순회하면서 출력하는데,
        print(card_left[i], end = " ")

        if len(card_right) > i :        # 홀수의 경우 마지막 인덱스에서 에러가 날 것이기 때문에 예외처리
            print(card_right[i], end = " ")
    print()