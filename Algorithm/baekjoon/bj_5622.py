test_case = input()
# 다이얼 dic 만듬
dial = {2 : ["A","B","C"], 3 : ['D','E','F'], 4 : ['G','H','I'], 5 : ['J','K','L'], 6 : ['M','N','O'], 7 : ['P','Q','R','S'], 8 : ['T','U','V'], 9 : ['W','X','Y','Z']}
output = 0

for i in test_case : #테스트 케이스 각 알파벳이
    for j in dial : #다이얼 dic 내에서
        if i in dial[j] : #몇번에 있나요?
            output += j+1 #다이얼에 숫자 없는 빈공간 +1 
print(output)