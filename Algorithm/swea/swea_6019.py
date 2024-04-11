t = int(input())

for i in range(t):
    D,A,B,F = map(int,input().split())

    print(f"#{i+1} {D/(A+B)*F}")