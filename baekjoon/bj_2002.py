import sys

input = sys.stdin.readline

N = int(input())

turnel_in = list(input().strip() for _ in range(N))
turnel_out = list(input().strip() for _ in range(N))


# 투포인터 방식
i = 0                                       # in 포인터
j = 0                                       # out 포인터
speeding = {}                               # 과속 단속 딕셔너리
cnt = 0                                     # 정답 세는 변수
while i != N and j != N :
    if turnel_in[i] == turnel_out[j]:       # 조건 1) 순서에 맞게 나왔다 들어감
        i+=1
        j+=1
                
    elif turnel_in[i] != turnel_out[j]:     # 조건 2) 순서에 맞지 않음

        # if turnel_in[i] in speeding :     # 조건 2-1) 늦게 나감   # 34028 kb / 64 ms
        if speeding.get(turnel_in[i], False):                     # 31120 kb / 40 ms
            i += 1                          # in 포인터 + 1

        else :                              # 조건 2-2) 먼저 나감
            speeding[turnel_out[j]] = True  # 과속 차량 등록
            j += 1                          # out 포인터 + 1
            cnt += 1                        # 카운트 올림
    
print(cnt)