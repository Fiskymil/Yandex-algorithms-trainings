seq = input()

counter = 0

for i in range(len(seq)):
    if counter >= 0:
        if seq[i] == '(':
            counter += 1
        else:
            counter -= 1
    else:
        break

if counter == 0:
    print('YES')
else:
    print('NO')
