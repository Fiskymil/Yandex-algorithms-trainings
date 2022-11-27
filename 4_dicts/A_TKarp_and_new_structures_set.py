n = int(input())
pairs_dict = {}

for i in range(n):
    a, b = map(int, input().split())
    if a in pairs_dict:
        pairs_dict[a] += b
    else:
        pairs_dict.update({a: b})

for key, value in sorted(pairs_dict.items()):
    print(key, value)
