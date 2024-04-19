rope = int(input('Введите кол-во веревок (введите 0 для завершения): '))
counter = 0

while rope != 0:
    if rope % 4 == 0:
        counter += 1
    rope = int(input('Введите кол-во веревок (введите 0 для завершения): '))

print(counter)