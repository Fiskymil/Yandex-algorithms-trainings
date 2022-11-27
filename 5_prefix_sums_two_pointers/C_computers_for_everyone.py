N, M = map(int, input().split())
x = list(map(int, input().split()))
y = list(map(int, input().split()))

out = [0] * N
unusej = set()
bestj = 0
for i in range(N):
    cur_val = 1001
    for j in range(M):
        if (y[j] - x[i] >= 1) and (y[j] - x[i] < cur_val) and (j not in unusej):
            out[i] = j + 1
            cur_val = y[j] - x[i]
            bestj = j
    unusej.add(bestj)
print(len([i for i, e in enumerate(out) if e != 0]))
print(*out)
