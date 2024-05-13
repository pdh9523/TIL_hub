N = int(input())
person = [ [*map(int,input().split())] for _ in range(N) ]

for man in person :
    rank = 1
    for other in person :
        if man[0] < other[0] and man[1] < other[1]: rank += 1
    print(rank, end=' ')