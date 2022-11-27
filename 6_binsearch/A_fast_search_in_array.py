def check_istrue(m, pararms):
    arr, numb = pararms
    if arr[m] >= numb:
        return True


def lbinsearch(l, r, check, checkpars):
    while l < r:
        m = (l + r) // 2
        if check(m, checkpars):
            r = m
        else:
            l = m + 1
    return l


N = int(input())
nums = list(map(int, input().split()))
nums.sort()
K = int(input())

while K != 0:
    L, R = map(int, input().split())
    params1 = nums, L
    params2 = nums, R + 1
    print(lbinsearch(0, N, check_istrue, params2) - lbinsearch(0, N, check_istrue, params1), end=' ')
    K -= 1

