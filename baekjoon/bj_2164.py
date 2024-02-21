from collections import deque

card = deque(range(1,int(input())+1))

while card :
    if card :
        left = card.popleft()
    if card :
        card.append(card.popleft())

print(left)