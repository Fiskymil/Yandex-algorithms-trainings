r = int(input())
i = int(input())
c = int(input())

if i == 0:
    print(3) if r != 0 else print(c)
elif i == 1:
    print(c)
elif i == 4:
    print(3) if r!= 0 else print(4)
elif i == 6:
    print(0)
elif i == 7:
    print(1)
else:
    print(i)
# Если интерактор выдал вердикт 0, итоговый вердикт равен 3 в случае, если программа завершилась с ненулевым кодом, и вердикту чекера в противном случае.
# Если интерактор выдал вердикт 1, итоговый вердикт равен вердикту чекера.
# Если интерактор выдал вердикт 4, итоговый вердикт равен 3 в случае, если программа завершилась с ненулевым кодом, и 4 в противном случае.
# Если интерактор выдал вердикт 6, итоговый вердикт равен 0.
# Если интерактор выдал вердикт 7, итоговый вердикт равен 1.