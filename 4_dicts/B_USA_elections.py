pairs_dict = {}

while True:
    try:
        a, b = map(str, input().split())
        b = int(b)
        if a in pairs_dict:
            pairs_dict[a] += b
        else:
            pairs_dict.update({a: b})
    except:
        break

for key, value in sorted(pairs_dict.items()):
    print(key, value)
