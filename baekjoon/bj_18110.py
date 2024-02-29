import sys
from collections import deque

def halfceil(num):
    if int(num) <= num - 0.5 :
        return int(num)+1
    else :
        return int(num)

t = int(input())

excl  = halfceil(t*0.15)
output = list()
for _ in range(t) :
    output.append(int(sys.stdin.readline().strip()))

output.sort()
output = deque(output)

for _ in range(excl):
    output.pop()
    output.popleft()


if t==0:
    print(0)
else :
    ans = sum(output) / (t - (2*excl))
    print(halfceil(ans))

### 괜히 어렵게 생각하지 마세요
    
# t = int(input())

# excl = halfceil(t*0.15)

# under = []
# upper = []

# output = 0
# for _ in range(t):
#     tier = int(sys.stdin.readline().strip())
    
#     if excl == 0 :
#         output += tier
#     else :
#         output += tier
#         if len(upper) < excl or tier > upper[-1] :
#             if len(upper) == excl:
#                 upper.pop()
#             upper.append(tier)
#             upper.sort(reverse=True)
#         if len(under) < excl or tier < under[-1] :
#             if len(under) == excl :
#                 under.pop()
#             under.append(tier)
#             under.sort()
# if t == 0 :
#     print(0)
# else :
#     print(halfceil((output-sum(under)-sum(upper))/ (t-(2*excl))))

