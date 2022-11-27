from math import pi

n = int(input())
events = []
rmin = 0
rmax = 10 ** 6

for i in range(1, n + 1):
    r1, r2, phi1, phi2 = map(float, input().split())
    rmin = max(r1, rmin)
    rmax = min(r2, rmax)
    events.append((phi1, -i))
    events.append((phi2, i))
events.sort()

uset = set()
segs = 0

for ev in events:
    if ev[1] < 0:
        segs += 1
        uset.add(-ev[1])
    elif ev[1] in uset:
        segs -= 1

square = 0

for i in range(len(events)):
    ev = events[i]
    if ev[1] < 0:
        segs += 1
    else:
        segs -= 1
    if segs == n:
        if i < len(events) - 1:
            square += (events[i + 1][0] - events[i][0]) * (rmax ** 2 - rmin ** 2) / 2
        else:
            square += (events[0][0] - events[len(events) - 1][0] + 2 * pi) * (rmax ** 2 - rmin ** 2) / 2
print(square)
