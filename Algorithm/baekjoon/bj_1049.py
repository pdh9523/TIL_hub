n,m = map(int,input().split(" "))
pack_n = n//6
one_n = n%6
cheap_pack = 1000
cheap_one = 1000

for i in range(m) :
    pack, one = map(int,input().split(" "))
    if pack < cheap_pack :
        cheap_pack = pack
    if one < cheap_one :
        cheap_one = one
if cheap_one * one_n > cheap_pack :
    pack_n += 1
    one_n = 0
result = cheap_one*one_n + cheap_pack*pack_n    
if cheap_pack > cheap_one * 6 :
    result = n*cheap_one

print(result)