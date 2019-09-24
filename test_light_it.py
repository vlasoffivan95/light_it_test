import random


class Sample(object):  # Основной класс, который содержит объекты игрока и компьютера
    health = 100

    def first_move(self, object1):  # Первый возможный вариант хода
        object1.health -= random.randint(18, 25)

    def second_move(self, object1):  # Второй возможный вариант хода
        object1.health -= random.randint(10, 35)

    def third_move(self):  # Третий возможный вариант хода
        self.health += random.randint(18, 25)


bot = Sample()  # Создание объекта компьютера
player = Sample()  # Создание объекта игрока
while bot.health > 0 and player.health > 0:
    # Вывод необходимой информации, включая очередь хода, здоровье каждого персонажа и вариации хода
    turn = random.choice([True, False])
    print("Текущее положение\n\nХодит {0}Здоровье Компьютера:   {1}\nЗдоровье Игрока:   {2}\n".format((
        "игрок\n\n" if turn else "компьютер\n\n"), str(bot.health), str(player.health))

    )
    # Ход игрока
    if turn:
        print("1 - Противнику наносится урон в размере от 18 до 25 \n"
              "2 - Противнику наносится урон в размере от 10 до 35 \n"
              "3 - Вы пополняете себе здоровье в размере от 18 до 25 \n"
              "Введите число, под которым находится ваш ход: ")
        move = int(input())
        while move != 1 and move != 2 and move != 3:
            move = int(input())
        if move == 1:
            player.first_move(bot)
        if move == 2:
            player.second_move(bot)
        if move == 3:
            player.third_move()
    # Ход компьютера
    else:
        move = random.randint(1, 3)
        # Увеличение шанса на избрание третьего хода
        if bot.health <= 30 and move != 3:
            move = random.randint(1, 3)
        if move == 1:
            bot.first_move(player)
        if move == 2:
            bot.second_move(player)
        if move == 3:
            bot.third_move()

# Вывод с информацией о победе
if bot.health <= 0:
    print("Вы победили, ваше здровье в момент победы составляло " + str(player.health))

if player.health <= 0:
    print("Вы проиграли, здровье компьютера в момент победы составляло " + str(bot.health))