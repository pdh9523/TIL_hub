# 1이 밑으로(오른쪽) 2가 위로 (왼쪽)
for idx in range(1,11):

    t = int(input())
    tables = [map(int,input().split()) for _ in range(t)]
    tables = [char for char in zip(*tables)]
    cnt = 0
    for table in tables:
        check = False
        for char in table :
            if char == 1 :
                check = True
            elif char == 2 and check :
                cnt += 1
                check = False
    print(f"#{idx} {cnt}")