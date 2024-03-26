from itertools import permutations

N = int(input())        

a,b = map(int,input().split())
professor = a*b // 100

table = dict()
ans_table = dict()
for idx in range(1,N+1):
    team1 = input().split()
    team2 = input().split()

    t1 = int(team1[0]) * int(team1[1]) // 100
    if team1[2] == "K":
        t1 *= 0.7
    t2 = int(team2[0]) * int(team2[1]) // 100
    if team2[2] == "K":
        t2 *= 0.7

    result = int((t1+t2)//2)
    
    table[f"{team1[3]} {team2[3]} ({idx}팀)"] = (result,idx)

for key in table :                                      
    if len(str(table[key][0])) == 2:
        a = permutations(str(table[key][0])+"0", 3)
        
    else :
        a = permutations(str(table[key][0]), 3)
    
    min_value = float('inf')
    
    for i in a :
        print("".join(i))
        tmp = abs(professor - int("".join(i)))
        min_value = min(abs(min_value),tmp)
    
    ans_table[key] = (abs(min_value), -table[key][0], table[key][1])   # 비교를 위해 환산점수 , 원점수(음수)로 저장

ans_table = {value:key for key,value in ans_table.items()}


temp = sorted(ans_table)    # 여기서 원점수 음수로 해야 큰 수가 앞으로 분류됩니다

for i in range(N):
    print(f"{i+1}등 : {ans_table[temp[i]]}")