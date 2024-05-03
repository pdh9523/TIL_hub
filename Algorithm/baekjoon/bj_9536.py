import sys

input = sys.stdin.readline


for _ in range(int(input())):

    howles = input().split()

    others = dict()

    while True :
        what = input().strip()
        if what == "what does the fox say?":
            break

        data = what.split(" goes ")
        others[data[1]] = 1
    
    for howl in howles:
        if others.get(howl):
            continue
        print(howl, end=" ")