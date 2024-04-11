a = int(input())
# {key : [value,value,value ...]}
test_dict = {}
for i in range(a) :
    t_key,t_value = map(int,input().split())
    if t_key in test_dict :
        test_dict[t_key].append(t_value)
    else : 
        test_dict[t_key] = [t_value]
        
rem = list(test_dict.keys())
rem.sort() # 키 정리
for i in rem :
    test_dict[i].sort() #딕셔너리 내부 리스트 정리

for x in rem :
    for y in test_dict[x] :
        print(f"{x} {y}")