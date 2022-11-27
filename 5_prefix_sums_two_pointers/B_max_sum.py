n = int(input())
a = list(map(int, input().split()))

prefixsum = [0] * (n + 1)
maxsum = -10000000000
minsum = 0

for i in range(1, n + 1):
    prefixsum[i] = prefixsum[i - 1] + a[i - 1]
    cursum = prefixsum[i] - minsum
    if prefixsum[i] < minsum:
        minsum = prefixsum[i]
    if cursum > maxsum:
        maxsum = cursum

print(maxsum)
