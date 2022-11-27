elect_dict_init = {}
elect_dict = {}
with open('input.txt', 'r') as elects:
    for line in elects:
        elect_dict_init.update({' '.join(line.split()[0:-1]): int(line.split()[-1])})

vote_const = sum(elect_dict_init.values()) / 450
elect_dict.update({key: value // vote_const for key, value in elect_dict_init.items()})

if sum(elect_dict.values()) < 450:
    vote_dif = 450 - sum(elect_dict.values())
    elect_list = [[k % vote_const, k, k // vote_const, v] for v, k in elect_dict_init.items()]

    for el in sorted(elect_list, key=lambda x: (x[0], -x[1]), reverse=True):
        if vote_dif != 0:
            el[2] = el[2] + 1
            vote_dif -= 1

    for el in elect_list:
        print(el[3], int(el[2]))
else:
    for key, value in sorted(elect_dict.items()):
        print(key, int(value))
