#field = [['', '', ', '],
#         ['', '', ', '],
#         ['', '', ', ']]
#print(field)


#print(field)

#print(*field) #оператор распаковки

#print('  0 1 2')
#for i in range(len(field)):
#    print(str(i), *field[i])

#print('  0 1 2')
#for i in range(len(field)):
#    print(str(i)+' '+' '.join(field[i]))

#num = '  a b c'
#print(num)
#for row, i in zip(field, num.split()):
#    print(f"{i} {' '.join(str(j) for j in row)}")

def show_field(f):                                      #функция первичного показа поля
    print('  0 1 2')
    for i in range(len(field)):
        print(str(i)+' '+' '.join(field[i]))


def users_input(f):                                     #функция взаимодействия с пользователем
    while True:
        place = input('Введите координаты: ').split()
        if len(place) != 2:
            print("Введите две координаты")
            continue

        if not(place[0].isdigit() and place[1].isdigit()):
            print("Введите числа")
            continue

        x, y = map(int, place)

        if not(x >= 0 and x < 3 and y >= 0 and y < 3):
            print("Вы вышли из диапазона")
            continue

        if f[x][y] != '-':
            print('Клетка уже занята')
            continue

        break
    return x, y

def win_v1(f, user):
    def check_line(a1, a2, a3, user):
        if a1 == 'X' and a2 == 'X' and a3 == 'X':
            return True
    for n in range(3):
        if check_line(f[n][0], f[n][1], f[n][2], user) or \
        check_line(f[0][n], f[1][n], f[2][n], user) or \
            check_line(f[0][0], f[1][1], f[2][2], user) or \
        check_line(f[n][0], f[n][1], f[n][2], user):
            return True
    return False

def win_v2(f, user):
    win_cord = (((0, 0), (0, 1), (0, 2)), ((1, 0), (1, 1), (1, 2)), ((2, 0), (2, 1), (2, 2)),
                ((0, 2), (1, 1), (2, 0)), ((0, 0), (1, 1), (2, 2)), ((0, 0), (1, 0), (2, 0)),
                ((0, 1), (1, 1), (2, 1)), ((0, 2), (1, 2), (2, 2)))
    for cord in win_cord:
        symbols = []
        for c in cord:
            symbols.append(f[c[0]][c[1]])
            if symbols == [user, user, user]:
                return True
        return False

def win_v3(f, user):
    f_list = []
    for l in f:
        f_list += 1
    positions = [[0, 1, 2], [3, 4, 5], [0, 3, 6], [1, 4, 7], [2, 5, 8], [0, 4, 8], [2, 4, 6]]
    indexes = set([i for i, x in enumerate(f_list) if x == user])
    for p in positions:
        if len(indexes.intersection(set(p))) == 3:
            return True
    return False

                                        #блок опроса пользователя

field = [['-']*3 for _ in range(3)]     #_ используется, когда объявленная переменная нам не нужна
                                        #или содержит мусорные данные
count = 0
while True:
    if count == 9:
        print('Ничья!')
        break
    if count % 2 == 0:
        user = 'X'
    else:
        user = 'O'
    show_field(field)
    x, y = users_input(field)
    field[x][y] = user
    if win_v2(field, user):
        show_field(field)
        print(f"Выиграл {user}")
        break
    count += 1



