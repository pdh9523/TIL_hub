gomgom = list(map(int,input().split()))     # 0 치킨 1 피자 2 햄버거
coupon = list(map(int,input().split()))

# 치킨 3 - > 피자 1 . 피자3 - > 햄버거 1 . 햄버거 3 -> 치킨 1.
idx = 0 
ans = 0
while idx != 6 :
    # 곰곰이가 식권보다 많은 경우
    if gomgom[(idx)%3] >= coupon[(idx)%3]:          
        ans += coupon[(idx)%3]
        gomgom[(idx)%3] -= coupon[(idx)%3]          # 곰곰이들 밥 사주기
        coupon[(idx)%3] = 0                         # 쿠폰을 다 써서
    # 식권이 곰곰이들보다 많은 경우
    elif gomgom[(idx)%3] and gomgom[(idx%3)] <= coupon[(idx)%3] :
        ans += gomgom[(idx)%3]                      
        coupon[(idx)%3] -= gomgom[(idx)%3]          # 쿠폰은
        gomgom[(idx)%3] = 0                         # 곰곰이들 밥 다 사주고
    # 식권 정리
    coupon[(idx+1)%3] += coupon[(idx)%3]//3     # 바꾸고
    coupon[(idx)%3] = coupon[(idx)%3]%3         # 나머지 챙겨두기
    # 로테 2번 돌면 끝날 듯
    idx += 1
print(ans)
