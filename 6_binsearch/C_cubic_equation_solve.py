def binsearch(l, r, eps):
    while r - l > eps:
        m = (l + r) / 2
        if f(m) * f(r) > 0:
            r = m
        else:
            l = m
    return l


def f(x):
    f = a * pow(x, 3) + b * pow(x, 2) + c * x + d
    return f


a, b, c, d = map(int, input().split())
eps = 1e-6
r = 1

if f(0) == 0:
    print(0)
else:
    while f(r) * f(-r) >= 0:
        r *= 2
    l = -r
    print(binsearch(l, r, eps))

