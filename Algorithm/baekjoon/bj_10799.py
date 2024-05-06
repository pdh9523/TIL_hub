txt,ans,cnt = input(),0,0
for i in range(len(txt)):
    if txt[i] == "(":
        cnt+=1
    else :
        if txt[i-1]=="(":
            cnt-=1;ans+=cnt
        else :
            cnt-=1;ans+=1
print(ans)