N = int(input())
folds = list(map(int, input().split()))
sec = 0
if N == 2:
    print(1)
else:
    folds.sort()
    for i in range(N - 1):
        sec += folds[i]
    print(sec)
