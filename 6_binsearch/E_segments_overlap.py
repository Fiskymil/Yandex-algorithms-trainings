n, k = map(int, input().split())
x = list(map(int, input().split()))
x.sort()

left = 0
right = x[-1] - x[0]


def lbinsearch(l, r, check):
    while l < r:
        m = (l + r) // 2
        if check(x, m):
            r = m
        else:
            l = m + 1
    return l


def checkfunc(x, m):
    cnt = 0
    maxright = x[0] - 1
    for el in x:
        if el > maxright:
            cnt += 1
            maxright = el + m
    if cnt <= k:
        return True


print((lbinsearch(left, right, checkfunc)))
