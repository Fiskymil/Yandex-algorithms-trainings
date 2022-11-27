d = int(input())
x1, x2 = map(int, input().split())

if x1 >= 0 and x2 >= 0 and (x1 + x2 <= d):
    print(0)
else:
    dist = [(x1 ** 2 + x2 ** 2, 1),
            ((x1 - d) ** 2 + x2 ** 2, 2),
            (x1 ** 2 + (x2 - d) ** 2, 3)]
    print(min(dist)[1])
