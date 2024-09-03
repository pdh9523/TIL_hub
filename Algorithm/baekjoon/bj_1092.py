N = int(input())
cranes = sorted([*map(int, input().split())], reverse=True)

M = int(input())
cargos = sorted([*map(int, input().split())], reverse=True)

# 모든 물건을 옮길 수 없으면 -1을 출력
if cargos[0] > cranes[0]: exit(print(-1))

cnt = 0
while True:
    check = True
    for crane in cranes:
        if crane < cargos[-1]: break

        for i in range(M):
            if cargos[i] == 0: continue

            if crane >= cargos[i]:
                cargos[i] = 0
                check = False
                break
    if check: break
    cnt += 1
print(cnt)
