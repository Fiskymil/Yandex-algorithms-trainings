L, K = map(int, input().split(sep=' '))
legs = list(map(int, input().split()))
cnt = 0
a = 0
b = 0
if L % 2 == 1 and L // 2 in legs:
    print(L // 2)
else:
    for i in range((L // 2) - 1, -1, -1):
        if i in legs:
            a = i
            break
    for i in range((L // 2), L):
        if i in legs:
            b = i
            break
    print(a, b)
