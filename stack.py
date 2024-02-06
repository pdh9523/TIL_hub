class Stack :
    def __init__(self, capacity) :
        self.capacity = capacity # capacity : 스택의 용량
        self.arr = [None]*self.capacity # arr : 스택 구조
        self.top = -1 # 최상단의 인덱스 표현

    def isEmpty(self) :
        return self.top == -1 # 최상단의 인덱스가 -1인 경우(비어있는 경우) True를 반환
    
    def isFull(self) :
        return self.top == self.capacity-1 # 최상단의 인덱스가 용량 -1 인 경우(꽉 찬 경우) True를 반환
    
    def push(self, item) : # push 연산
        if not self.isFull() : # 스택이 꽉 차있지 않으면
            self.top += 1 # 최상단의 인덱스를 하나 올리고
            self.arr[self.top] = item # 아이템을 배열에 집어넣는다
        else :
            pass
    
    def pop(self) : # pop 연산
        if not self.isEmpty() : # 스택이 비어있지 않으면
            self.top -=1  # 최상단의 인덱스를 하나 내리고
            return self.arr[self.top+1] # 그 아이템을 반환한다.
        else :
            pass

    def peek(self) : # peek 연산
        if not self.isEmpty() : # 스택이 비어있지 않으면
            return self.arr[self.top] # 최상단의 아이템을 확인한다.
        else :
            pass
    
    def size(self) :
        return self.top+1  #그냥 사이즈 확인하는 것
    

## 인덱스를 따로 두고 리스트를 처리하는 방식과 유사하다.

a = Stack(10)

t = "안녕하신지드"

for char in t :
    a.push(char)

while not a.isEmpty() : # 문자열 뒤집기
    print(a.pop(), end="")
