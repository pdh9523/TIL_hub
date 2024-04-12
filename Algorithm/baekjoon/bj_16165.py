import sys

input = sys.stdin.readline

N, M = map(int,input().split()) # N 걸그룹 M 문제

group = {}
member = {}

for _ in range(N):
    group_name = input().strip()

    group_members = []

    for _ in range(int(input())):
        group_member = input().strip()
        group_members.append(group_member)
        member[group_member] = group_name
    group_members.sort()
    group[group_name] = group_members

for _ in range(M):
    quiz = input().strip()
    if int(input()) == 1 :
        print(member[quiz])
    else :
        for girl in group[quiz]:
            print(girl)