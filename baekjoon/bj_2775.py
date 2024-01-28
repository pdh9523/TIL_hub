t = int(input())

def double(floor) :
    target_floor = []
    for i in range(1,len(floor)+1) :
        target_floor.append(sum(floor[:i]))
    return target_floor


for i in range(t) :
    floor = int(input())
    hosu = int(input())
    
    base_floor = [1] * hosu
    
    for j in range(floor+1) :
        base_floor = double(base_floor)
    
    print(base_floor[-1])