m = int(input())
segments = []

while True:
    l, r = map(int, input().split())
    if l == r == 0:
        break
    elif r > 0 and l < m:
        segments.append((l, r))

segments.sort()

ans = []
nowright = 0
nextright = 0
nowbest = 0, 0

for seg in segments:
    if seg[0] > nowright:
        ans.append(nowbest)
        nowright = nextright
    if nowright >= m:
        break
    if seg[0] <= nowright and seg[1] > nextright:
        nextright = seg[1]
        nowbest = seg

if nowright < m:
    nowright = nextright
    ans.append(nowbest)
if nowright < m:
    print('No solution')
else:
    print(len(ans))
    for seg in ans:
        print(*seg)
