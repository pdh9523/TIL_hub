io = "IO"
N, M= int(input()), int(input())
S = input()

P = io*N + "I"
L = len(P)
cnt = 0
# for i in range(M-L+1):
#     if S[i:i+L] == P :
#         cnt +=1 

# print(cnt)

# 슬라이스[a:b]에서 시간 복잡도는 O(b-a)
# 따라서 O(kn)의 시간복잡도 발생

# I O I 를 하나씩 순회
# S = 문자열 / P 는 타겟 문자열 / N 은 O 개수
idx = 0
ans = 0 
while idx != M-2:
    if S[idx] == "I":
        idx += 1
        if S[idx] == "O" and S[idx+1] == "I":
            idx += 1
            cnt+=1
        else :
            idx+=1
            ans += (cnt+1 - N) if (cnt+1)-N > 0 else 0
            cnt =0
    else :
        idx+=1
        ans += (cnt+1 - N) if (cnt+1)-N > 0 else 0
        cnt
print(ans)
## ???