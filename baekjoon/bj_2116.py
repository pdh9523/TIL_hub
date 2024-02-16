# A-F // B-D // C-E //

t = int(input())

test_list = [list(map(int,input().split())) for _ in range(t)]


# 튜플로 묶기?
a_f = []    
b_d = []    
c_e = []    

for lst in test_list:
    a_f.extend((lst[1:5]))
    b_d.append((lst[0],lst[2],lst[4],lst[5]))
    c_e.append((lst[0],lst[1],lst[3],lst[5]))

output = 0
for idx in range(t) :
    output += max(max(a_f[idx]),max(b_d[idx]),max(c_e[idx]))