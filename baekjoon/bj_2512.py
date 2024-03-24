N = int(input())

request = sorted(list(map(int,input().split())))

budget = int(input())

for town in request :
    if budget // N >= town:
        budget -= town
        N -= 1
if N == 0 :
    print(max(request))
else :
    print(budget // N)