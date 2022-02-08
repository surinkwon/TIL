while True:
    sen = input()

    if sen == '#':
        break

    total = 0
    for i in sen:
        if i in ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']:
            total += 1
    print(total)

