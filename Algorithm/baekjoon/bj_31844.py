S = input()
check = S.replace(".", "")
if check =="#@!" or check == "!@#" or check=="@!#" or check=="#!@": exit(print(-1))

print(abs(S.index("@")-S.index("!"))-1)