freq_dict = {}
with open('input.txt', 'r') as fin:
    for line in fin:
        letter_list = line.split()
        for letter in letter_list:
            freq_dict[letter] = freq_dict.get(letter, 0) + 1

letter_tuples = [(k, v) for v, k in freq_dict.items()]

for letter in sorted(letter_tuples, key=lambda x: (-x[0], x[1]), reverse=False):
    print(letter[1])
