x, y, w, s = map(int,input().split())
# x = 집의 x 좌표
# y = 집의 y 좌표
# w = 한칸 비용
# s = 2칸비용

if x < y : # x가 무조건 큽니다.
    x, y = y, x

# 조건 1) 한칸 비용이 2칸 비용보다 저렴한가?
# 조건 2) 그럼 무조건 2칸을 가는가?

if s > w*2 : # 2칸비용보다 한칸으로 2번 가는게 더 비싸면 ?
    print((x+y)*w) # 2칸 비용이 필요 없어질때까지 2칸으로 달리기
else :
    if s < w :  # 대각이 더 싸면 대각 위로 대각 아래로 조건이 가능함 
        print((y*s) + (((x-y) // 2) * 2*s) + (x-y) % 2 * w)
    else :
        print((y*s) + (x-y)*w)
        