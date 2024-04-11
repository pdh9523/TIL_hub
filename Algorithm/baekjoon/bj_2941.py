cr = ["c=","c-","dz=","d-","lj","nj","s=","z="]

a=input()

output = len(a)

for i in range(len(a)) :
    if a[i:i+3] in cr :
        output -= 1
    elif a[i:i+2] in cr :
        output -= 1
print(output)