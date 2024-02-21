import sys
from collections import deque

sys.stdin = open("1232.txt")

def post_order(node) :
    global output

    if len(tree[node]) >0:                         # 트리의 왼쪽 자손
        post_order(tree[node][0])

    if len(tree[node]) >1:                         # 트리의 오른쪽 자손
        post_order(tree[node][1])

    output.append(test_list[node])                 # 재귀 수렴 지점

for idx in range(1,11):

    t = int(input())
    tree = [None]                                  # 0 인덱스 채울 목적으로 None
    test_list = [None]     
    for _ in range(t):
        tc = input().split()
        tc.pop(0)                                  # 인덱스 부분 날리고
        test_list.append(tc.pop(0))                # 계산식은 test_list에 보관
        tree.append(list(map(int,tc)))             # 남은 것을 담으면 트리 지도
    
    # 루트의 정점은 항상 1
    
    output = deque()
    
    post_order(1)
    
    result_stack = []                              # 후위 계산식 계산법 재활용
    for char in output :
        if char.isdecimal():
            result_stack.append(char)
        else:
            b = int(result_stack.pop())
            a = int(result_stack.pop())
            
            if char == "+":
                result_stack.append(a+b)
            elif char == "-" :
                result_stack.append(a-b)
            elif char == "/" :
                result_stack.append(a//b)
            elif char == "*" :
                result_stack.append(a*b)
        
    print(f"#{idx}", *result_stack)         # 정상적인 방법으로 작동했다면 마지막에 값이 하나만 남을 것이고, 언패킹하면 된다.