N = int(input())

# 무서운 이야기 : (1,2)를 딕셔너리로 변환하면 {1:2}가 된다.w
correct = dict(zip(input().split(), range(N)))
# 이거랑 같음
# correct = dict()
# temp = input().split()
# i = 0
# for tmp in temp :
#     correct[tmp] = i
#     i += 1


test = input().split()

ans = 0
for i in range(N-1):
    for j in range(i+1,N):
        if correct.get(test[i]) < correct.get(test[j]):
            ans += 1

print(f"{ans}/{N*(N-1)//2}")