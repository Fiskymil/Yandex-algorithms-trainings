def lbinsearch(l, r, check, checkpars):
    while l < r:
        m = (l + r) // 2
        if check(m, checkpars):
            r = m
        else:
            l = m + 1
    return l


def rbinsearch(l, r, check, checkpars):
    while l < r:
        m = (l + r + 1) // 2
        if check(m, checkpars):
            l = m
        else:
            r = m - 1
    return l


def check_istruel(m, pararms):
    arr, numb = pararms
    if arr[m] >= numb:
        return True


def check_istruer(m, pararms):
    arr, numb = pararms
    if arr[m] <= numb:
        return True


N = int(input())
numarr = list(map(int, input().split()))
M = int(input())
searcharr = list(map(int, input().split()))

for el in searcharr:
    params = numarr, el
    firstleft = lbinsearch(0, N - 1, check_istruel, params)
    if numarr[firstleft] == el:
        print(firstleft + 1, end=' ')
    else:
        print(0, end=' ')
    firstright = rbinsearch(0, N - 1, check_istruer, params)
    if numarr[firstright] == el:
        print(firstright + 1, end='\n')
    else:
        print(0, end='\n')
