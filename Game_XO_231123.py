# Инструкция
print("Это игра в крестики-нолики.\n"
      "Выберите клетку куда поставить крестик или нолик.\n"
      "Для этого введите номер клетки, например '2'\n"
      "1|2|3\n"
      "4|5|6\n"
      "7|8|9")
# Конец инструкции

Game_table = {'1': ' ', '2': ' ', '3': ' ',
              '4': ' ', '5': ' ', '6': ' ',
              '7': ' ', '8': ' ', '9': ' '}

table_keys = []

for key in Game_table:
    table_keys.append(key)


def print_table(cell):
    print(cell['1'] + '|' + cell['2'] + '|' + cell['3'])
    print(cell['4'] + '|' + cell['5'] + '|' + cell['6'])
    print(cell['7'] + '|' + cell['8'] + '|' + cell['9'])


def game():
    print("Итак, начинаем игру. Таблица сейчас пуста")
    turn = 'X'
    count = 0

    for i in range(10):
        print_table(Game_table)
        print("Введите номер клетки для " + turn)

        move = input()

        if Game_table[move] == ' ':
            Game_table[move] = turn
            count += 1
        else:
            print("Эта клетка занята! Введите новый номер клетки:")
            continue

        # Проверяем кто победил
        if count >= 5:
            if Game_table['1'] == Game_table['2'] == Game_table['3'] != ' ':
                print_table(Game_table)
                print("Игра закончена. Победили: " + turn)
                break
            elif Game_table['4'] == Game_table['5'] == Game_table['6'] != ' ':
                print_table(Game_table)
                print("Игра закончена. Победили: " + turn)
                break
            elif Game_table['7'] == Game_table['8'] == Game_table['9'] != ' ':
                print_table(Game_table)
                print("Игра закончена. Победили: " + turn)
                break
            elif Game_table['1'] == Game_table['4'] == Game_table['7'] != ' ':
                print_table(Game_table)
                print("Игра закончена. Победили: " + turn)
                break
            elif Game_table['2'] == Game_table['5'] == Game_table['8'] != ' ':
                print_table(Game_table)
                print("Игра закончена. Победили: " + turn)
                break
            elif Game_table['3'] == Game_table['6'] == Game_table['9'] != ' ':
                print_table(Game_table)
                print("Игра закончена. Победили: " + turn)
                break
            elif Game_table['7'] == Game_table['5'] == Game_table['3'] != ' ':
                print_table(Game_table)
                print("Игра закончена. Победили: " + turn)
                break
            elif Game_table['1'] == Game_table['5'] == Game_table['9'] != ' ':
                print_table(Game_table)
                print("Игра закончена. Победили: " + turn)
                break

        if count == 9:
            print("Игра закончена.Это ничья!")

        if turn == 'X':
            turn = 'O'
        else:
            turn = 'X'

    restart = input("Хотите начать игру с начала? Введите yes или no: ")

    if restart == "yes":
        for key in table_keys:
            Game_table[key] = " "
        game()


game()
