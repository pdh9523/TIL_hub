from itertools import combinations

def dist(h,c):                                      # dist : 각 집과 치킨집 사이의 최소거리를 계산해 반환하는 함수
    ans = 0                                         # ans : 각각의 집과 치킨집 사이의 최소거리의 합
    for i in h:                                     # h: home
        tmp = 0                                     # tmp : 한 집과 치킨집 사이의 거리를 담은 임시 변수
        temp = float('inf')                         # temp : 한 집과 치킨 집 간 최소값을 담은 임시 변수
        for j in c:                                 # c: chicken
            tmp = abs(i[0]-j[0])+abs(i[1]-j[1])
            temp = min(temp,tmp)
        ans += temp
    return ans


N,M = map(int,input().split())
home, chicken, land = [], [], []

for i in range(N):
    city = list(map(int,input().split()))
    land.append(city)
    for key in enumerate(city):
        if key[1] == 1:                     # 1 : 집
            home.append((i,key[0]))
        elif key[1] == 2:                   # 2 : 치킨집
            chicken.append((i,key[0]))
            
chicken = combinations(chicken,M)           # 백트래킹? 귀찮습니다. 
min_value = float('inf')
for t in chicken:
    min_value = min(min_value,dist(home,t))

print(min_value)