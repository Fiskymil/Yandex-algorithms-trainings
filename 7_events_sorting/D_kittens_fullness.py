n, m = map(int, input().split())
events = [(el, 0) for el in list(map(int, input().split()))]
events_dict = {}
events_raw = []

for i in range(m):
    l, r = map(int, input().split())
    events.extend([(l, -1), (r, 1)])
    events_raw.append((l, r))
    events_dict.update({(l, -1): 0, (r, 1): 0})

events.sort()
countcats = 0

for event in events:
    if event[1] == 0:
        countcats += 1
    else:
        events_dict[(event[0], event[1])] = countcats

for event in events_raw:
    print(events_dict[(event[1], 1)] - events_dict[(event[0], -1)], end=' ')
