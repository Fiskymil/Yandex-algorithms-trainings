N = int(input())
homes = list(map(int, input().split()))
dist = [0]*N

for i in range(N):
    for j in range(N):
        dist[i] += abs(homes[i]-homes[j])

print(homes[dist.index(min(dist))])