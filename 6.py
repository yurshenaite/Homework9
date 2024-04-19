for ab in range(10, 100):
    cab = str(ab ** 2)
    if len(cab) == 3 and cab[1] == str(ab)[0] and cab[2] == str(ab)[1]:
        print(cab)