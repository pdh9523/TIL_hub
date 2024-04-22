import sys
input = sys.stdin.readline

N = int(input())
students = sorted([ int(input()) for _ in range(N)])
print(sum(map(lambda x : abs(students[x] - (x+1)), range(N))))