n = int(input())
segments = []
for i in range(n):
    l, r = map(int, input().split())
    segments.append((l, -1))
    segments.append((r, 1))

segments.sort()
filled = 0
flength = 0

for i in range(len(segments)):
    if filled > 0:
        flength += segments[i][0] - segments[i - 1][0]
        if segments[i][1] == 1:
            filled -= 1
        else:
            filled += 1
    elif segments[i][1] == -1:
        filled += 1
    else:
        filled -= 1
print(flength)
