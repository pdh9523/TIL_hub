t = int(input())

for idx in range(t):
    card, s = map(int,input().split())
    deck = list(range(1,card+1))
    overhand = int(card*0.37)
    perfect = int(card*0.5)
    for _ in range(s):
        for _ in range(overhand):
            deck.insert(0, deck.pop())
        
        upper = deck[:card-perfect]
        lower = deck[card-perfect:]
        deck = []
        while upper or lower :
            if upper :
                deck.append(upper.pop(0))
            if lower :
                deck.append(lower.pop(0))
    print(f"#{idx+1}", *deck)