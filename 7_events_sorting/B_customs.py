N = int(input())
customlist = []
for i in range(N):
    t, l = map(int, input().split())
    customlist.append((t, -1))
    customlist.append((t + l, 1))

machines_count = 0
curcargos = 0

for cust in sorted(customlist, key=lambda x: (x[0], -x[1])):
    if cust[1] == -1:
        curcargos += 1
        if machines_count < curcargos:
            machines_count += 1
    elif cust[1] == 1:
        curcargos -= 1
print(machines_count)
