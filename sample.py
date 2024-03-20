N = list(input())
len_N = len(N)
int_N = int(''.join(N))
M = int(input())

candidate = [abs(int_N - 100)]

if M > 0:
    broken = list(map(int, input().split()))
    N_broken = [0] * len_N

    for i in range(len_N):
        N[i] = int(N[i])
        if N[i] in broken:
            N_broken[i] = 1

    if len(N_broken) == 0:
        candidate.append(len_N)
    else:
        for k in [-1, 1]:   # 더하거나 빼는 두가지 경우를 확인
            near_N = int_N
            while 0 <= near_N + k < 10**(len_N+1):
                near_N += k
                for j in range(len(str(near_N))):
                    if int(str(near_N)[j]) in broken:
                        break
                else:       # 모든 자리의 수를 누를 수 있는 번호 발견
                    candidate.append(len(str(near_N)) + abs(near_N - int_N))
                    break

else:
    candidate.append(len_N)

print(min(candidate))