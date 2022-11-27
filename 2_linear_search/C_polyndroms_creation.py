string = input()
tugs = 0
lens = len(string)
for i in range(len(string)//2):
    if string[i] != string[lens - i-1]:
        tugs += 1
print(tugs)
