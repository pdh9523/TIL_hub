import sys; input = sys.stdin.readline


N, K = map(int, input().split())
particles = [[*map(int,input().split())] for _ in range(N)]

red = particles[0]
particles.sort()

idx = particles.index(red)

positions = sorted([p+t*K for p,t in particles])
print(positions[idx])
