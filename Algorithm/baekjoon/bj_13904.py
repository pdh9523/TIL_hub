import sys
input = sys.stdin.readline


class queue() :
    def __init__ (self,capacity) :
        self.capacity = capacity
        self.arr = [-1]*self.capacity
        self.top = -1
        self.first = 0

    def push (self, item) :
        self.top += 1
        self.arr[self.top] = item

    def front(self):
        return self.arr[self.first]
    
    def back(self):
        return self.arr[self.top]

    def empty(self):
        return self.first==self.top+1

    def pop(self):
        self.first += 1
        return self.arr[self.first-1]
    
    def size(self):
        return self.top-self.first+1

N = int(input())

q = queue(N)

for _ in range(N):
    order, *a = input().split()
    if order == "push":
        q.push(*a)
    elif order == "pop":
        if q.empty() :
            print(-1)
        else :
            print(q.pop())

    elif order == "size":
        print(q.size())
    elif order == "empty":
        print(int(q.empty()))
    elif order == "front":
        if q.empty() :
            print(-1)
        else :
            print(q.front())
    elif order == "back":
        if q.empty() :
            print(-1)
        else :
            print(q.back())