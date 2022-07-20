print("****Добро пожаловать в игру 'Крестики нолики!'****")
print("---------------------------------------------------")
print("ПРАВИЛА ИГРЫ: ")
print("------------------------------")
print("Игроки делают ходы по очереди добиваясь "
      "заполнения трех подряд идущих клеток,"
      "которые могут располагаться по горизонтали, "
      "вертикали или диагонали.")
print("------------------------------------------------")
print("Чтобы сделать ход необходимо через пробел ввести"
      " две координаты клетки через пробел.")
print("Сначала вводится номер строки, затем номер столбца.")
print("---------------------------------------------------")
print("Удачи!")
print()
def show_field(f):                                      #функция первичного показа поля
    print('  0 1 2')
    for i in range(len(field)):
        print(str(i)+' '+' '.join(field[i]))


def users_input(f):                                     #функция взаимодействия с пользователем
    while True:
        place = input('Введите координаты: ').split()
        if len(place) != 2:
            print("Неверный ввод, ведите две координаты!")
            continue

        if not(place[0].isdigit() and place[1].isdigit()):
            print("Неверный ввод, ведите числа!")
            continue

        x, y = map(int, place)

        if not(x >= 0 and x < 3 and y >= 0 and y < 3):
            print("Ой, Вы вышли из диапазона координат клеток =(")
            continue

        if f[x][y] != '-':
            print('К сожалению, клетка уже занята =(')
            continue

        break
    return x, y

def win(f, user):                                     #функция определения победителя
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
    if win(field, user):
        show_field(field)
        print(f"Выиграл игрок {user} поздравляем!")
        break
    count += 1



