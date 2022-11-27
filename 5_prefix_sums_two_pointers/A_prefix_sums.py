n, q = map(int, input().split())  # размер массива и кол-во запросов
a = list(map(int, input().split()))  # массив
prefixsum = [0] * (n + 1)

for i in range(1, n + 1):
    prefixsum[i] = prefixsum[i - 1] + a[i - 1]

for i in range(q):
    l, r = map(int, input().split())
    print(prefixsum[r] - prefixsum[l - 1])
