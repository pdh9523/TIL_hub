N = int(input())
S = input()
while "PS5" in S or "PS4" in S:
    if "PS5" in S:
        S = S.replace("PS5", "PS")
    elif "PS4" in S:
        S = S.replace("PS4", "PS")

print(S)