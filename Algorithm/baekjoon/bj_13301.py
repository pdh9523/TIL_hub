def TEMP(TMP):
    if TMP in temp:
        return temp[TMP]
    
    temp[TMP] = TEMP(TMP-1) + TEMP(TMP-2)
    return temp[TMP]


temp = dict()
TMP = int(input())
temp[0] = 1
temp[1] = 1
print(TEMP(TMP+1)*2)