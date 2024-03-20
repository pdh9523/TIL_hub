import sys
input = sys.stdin.readline

for t in range(int(input())):
    N = int(input())
    stock = list(map(int, input().split()))

    sell = []
    for i in range(1, N):
        if i < N-1:
            if stock[i-1] < stock[i] and stock[i] > stock[i+1]:
                sell.append([stock[i], i])
        else:
            if stock[i-1] < stock[i]:
                sell.append([stock[i], i])

    sell.sort(key=lambda x: x[0], reverse=True)

    if len(sell) == 0:
        print(0)
    else:
        profit = 0
        last_i = -1
        end = -1
        for i in range(len(sell)):
            if sell[i][1] > last_i:
                last_i = sell[i][1]
                start = end + 1
                end = sell[i][1]
                for k in range(start, end):
                    profit += sell[i][0] - stock[k]
                if i != len(sell) - 1:
                    start = sell[i][1] + 1
                else:
                    break

        print(profit)