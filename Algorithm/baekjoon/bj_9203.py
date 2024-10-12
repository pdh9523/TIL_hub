import sys; input = sys.stdin.readline
from datetime import datetime


def cal_minutes(day, time):
    dt = datetime.strptime(day + " " + time, "%Y-%m-%d %H:%M")
    return int(dt.timestamp() // 60)

for _ in range(int(input())):
    B, C = map(int, input().split())
    
    events = []

    for _ in range(B):
        cd, start_day, start_time, end_day, end_time = input().split()
        start_minutes = cal_minutes(start_day, start_time)
        end_minutes = cal_minutes(end_day, end_time)

        events.append((start_minutes, 1))
        events.append((end_minutes+C, -1))
    
    events.sort()

    max_room=0
    cur_room=0
    
    for time, event in events:
        cur_room += event
        max_room = max(max_room, cur_room)
    
    print(max_room)