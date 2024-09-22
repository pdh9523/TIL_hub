# def is_prime(num):
#     if num <= 1:
#         data[num] = False
#         return False
    
#     if data[num]:
#         tmp = num*2
#         while tmp <= 2000000:
#             data[tmp] = False
#             tmp += num
#         return True
#     return False

# data = [True]*2000001



# N,M = map(int,input().split())
# for i in range(1,2000001):
#     ans = []
#     for j in range(N):
#         if not is_prime(i+j*M):
#             ans.append(i+j*M)
#         else: break
#     else:
#         exit(print(*ans))

N,M=map(int,input().split())
for i in range(2,N+2):
    print(M*i, end=" ")