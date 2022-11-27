M = int(input())
witness = []
for i in range(M):
    witness.append(set(input()))
N = int(input())
cnt_list = []
dange_list = []

for i in range(N):
    count = 0
    danger_car = input()
    dange_list.append(danger_car)
    danger_car = set(danger_car)
    for number in witness:
        if number.issubset(danger_car):
            count += 1
    cnt_list.append(count)
max_number = max(cnt_list)

for el1, el2 in zip(dange_list, cnt_list):
    if el2 == max_number:
        print(el1)
