input_file = open('input.txt', 'r')
list_input = []
for line in input_file:
    if line != '0\n':
        list_input.append(int(line))
    else:
        break
input_file.close()
max_el = list_input[0]
count = 1
for el in list_input[1:]:
    if el > max_el:
        max_el = el
        count = 1
    elif el == max_el:
        count += 1
print(count)
