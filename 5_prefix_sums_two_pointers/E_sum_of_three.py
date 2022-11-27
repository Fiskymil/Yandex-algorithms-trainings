def create_arr():
    arr = list(map(int, input().split()))
    n = arr[0]
    arr = sorted([j, i] for i, j in enumerate(arr[1:]))
    return arr, n


S = int(input())

A, n1 = create_arr()
B, n2 = create_arr()
C, n3 = create_arr()

ans_list = []
C.sort(key=lambda x: (x[0], -x[1]))
flag = False

for aval, apos in A:
    cpos = n3 - 1
    for bval, bpos in B:
        while cpos > 0 and aval + bval + C[cpos][0] > S:
            cpos -= 1
        if aval + bval + C[cpos][0] == S and (not flag or (apos, bpos, cpos)<ans):
            ans = apos, bpos, C[cpos][1]
            flag = True
if flag:
    print(*ans)
else:
    print(-1)
