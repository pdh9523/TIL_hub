t = int(input())

for i in range(t) :
    length = int(input())
    target = input().split('0') # 0을 스플릿하면 '' 으로 나눠짐
    target_list = list(map(len, target)) # target의 길이를 매핑해서 리스트로 다시 만듬
    print(f"{i+1} {max(target_list)}") 