data=["abc","def","ghi","jkl","mno","pqrs","tuv","wxyz"]

arr = [0]+[*map(int,input().split())]
S = input()
ans = ""
for char in S:
    for i in range(len(data)):
        if char in data[i]:
            if ans and ans[-1] == str(arr.index(i+2)): ans += "#"
            for _ in range(data[i].index(char)+1):
                ans += str(arr.index(i+2))
print(ans)