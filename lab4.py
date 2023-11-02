import random


def take_stones(stones):
    # Проверка наличия камней
    if stones <= 0:
        return False

    # Ход игрока
    print("Осталось", stones, "камней.")
    taken = int(input("Сколько камней вы берете? (1-3): "))

    # Проверка валидности хода
    if taken < 1 or taken > 3 or taken > stones:
        print("Некорректный ход. Попробуйте еще раз.")
        return take_stones(stones)

    # Обновление количества камней
    stones -= taken

    return stones


def play_game():
    # Генерация случайного числа камней
    stones = random.randint(4, 30)

    # Основной игровой цикл
    while stones > 0:
        # Ход первого игрока
        stones = take_stones(stones)

        # Проверка победы первого игрока
        if stones == 0:
            print("Вы победили!")
            break

        # Ход второго игрока
        taken = random.randint(1, 3)
        print("Соперник взял", taken, "камней.")

        # Обновление количества камней
        stones -= taken

        # Победа второго игрока
        if stones <= 0:
            print("Соперник победил!")


# Запуск игры
play_game()