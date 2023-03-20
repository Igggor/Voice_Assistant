def print_field(a):
    for b in a:
        print('-------------')
        print('|', b[0], '|', b[1], '|', b[2], '|')
    print('-------------')


def pick_winner(a):
    Answer = True
    for line in a:
        for elem in line:
            if line.count(elem) == 3 and elem != '-':
                Answer = elem
                return Answer  # Горизонт
    if a[0][0] == a[1][1] and a[0][0] == a[2][2] and a[0][0] != '-':
        Answer = a[0][0]
        return Answer
    if a[0][2] == a[1][1] and a[0][2] == a[2][0] and a[0][2] != '-':
        Answer = a[0][2]
        return Answer
    s = [[0] * 3 for u in range(3)]
    for i in range(3):
        for j in range(3):
            s[i][j] = a[j][i]
    for line in s:
        for elem in line:
            if line.count(elem) == 3 and elem != '-':
                Answer = elem
                return Answer
    return Answer


field = [['-'] * 3 for i in range(3)]
print_field(field)
Answer = True
hod = 'X'
while Answer == True:
    Answer = pick_winner(field)

    if hod == 'X':
        print('Ходят Крестики')
        str = int(input('Введите строку\n'))
        if(str > 3 or str < 1):
            print("Вы ввели неверное значение. Число должно принадлежать отрезку [1; 3]")
            str = int(input('Введите строку\n'))
        stolb = int(input('ведите столбец\n'))
        if (stolb > 3 or stolb < 1):
            print("Вы ввели неверное значение. Число должно принадлежать отрезку [1; 3]")
            stolb = int(input('Введите строку\n'))
        if field[str - 1][stolb - 1] == '-':
            field[str - 1][stolb - 1] = 'X'
            hod = '0'
        else:
            print('Тут уже занято')
        print_field(field)
        Answer = pick_winner(field)
    if hod == '0':
        print('Ходят Нолики')
        str = int(input('Введите строку\n'))
        if (str > 3 or str < 1):
            print("Вы ввели неверное значение. Число должно принадлежать отрезку [1; 3]")
            str = int(input('Введите строку\n'))
        stolb = int(input('ведите столбец\n'))
        if (stolb > 3 or stolb < 1):
            print("Вы ввели неверное значение. Число должно принадлежать отрезку [1; 3]")
            stolb = int(input('Введите строку\n'))
        if field[str - 1][stolb - 1] == '-':
            field[str - 1][stolb - 1] = '0'
            hod = 'X'
        else:
            print('Тут уже занято')
        print_field(field)

print('Победил', Answer)