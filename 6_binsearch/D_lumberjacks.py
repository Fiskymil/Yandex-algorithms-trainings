A, K, B, M, X = map(int, input().split())


def lbinsearch(l, r, check):
    while l < r:
        m = (l + r) // 2
        if check(m):
            r = m
        else:
            l = m + 1
    return l


def trees_to_day(m):
    trees = m * (A + B) - A * (m // K) - B * (m // M)
    if X <= trees:
        return True


max_days = X * 2 // (min(A, B)) + 1

print(lbinsearch(1, max_days, trees_to_day))
