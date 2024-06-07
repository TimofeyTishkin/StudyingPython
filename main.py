from random import randint
from math import log, ceil


def is_valid(n, ran):
    if n.isdigit():
        return 1 <= int(n) <= ran
    else:
        return False


print("Добро пожаловать в числовую угадайку!")
will = "Да"
while will.lower() == "да":
    print("До какого числа будем загадывать?")
    limit = input()
    while not limit.isdigit():
        print("Боюсь это не число... Попробуй еще разок.")
    limit = int(limit)
    tries = ceil(log(limit)/log(2))
    print("Я загадываю число... У вас есть {} попыток его угадать!".format(tries))
    number = randint(1, limit)
    for i in range(tries):
        guess = input()
        if not is_valid(guess, limit):
            print("А может быть все-таки введем целое число от 1 до {}?".format(limit))
            continue
        else:
            guess = int(guess)
        if guess == number:
            print("Вы угадали, поздравляем!")
            break
        elif guess < number:
            if tries - i -1 == 0:
                print("Вы не угадали. К сожалению попытки закончились :(")
                break
            print("Ваше число меньше загаданного, попробуйте еще разок. У вас есть ещё {} попыток его угадать!"
                  .format(tries-i-1))
        else:
            if tries - i -1 == 0:
                print("Вы не угадали. К сожалению попытки закончились :(")
                break
            print("Ваше число больше загаданного, попробуйте еще разок. У вас есть ещё {} попыток его угадать!"
                  .format(tries-i-1))

    print("Спасибо, что играли в числовую угадайку. Хотите сыграть еще?")
    will = input()
