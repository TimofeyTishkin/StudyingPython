from random import*


word_list = ["Автомобиль", "Полураспад", "Чемпионат", "Пиромания", "Цукцванг", "Звичензук", "Конкатенация",
             "Терминатор", "Деферент", "Градиент", "Производная", "Программирование", "Фейерверк", "Аспирантура"]


def display_hangman(tries):
    stages = [  # финальное состояние: голова, торс, обе руки, обе ноги
                '''
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     / \\
                   -
                ''',
                # голова, торс, обе руки, одна нога
                '''
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     / 
                   -
                ''',
                # голова, торс, обе руки
                '''
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |      
                   -
                ''',
                # голова, торс и одна рука
                '''
                   --------
                   |      |
                   |      O
                   |     \\|
                   |      |
                   |     
                   -
                ''',
                # голова и торс
                '''
                   --------
                   |      |
                   |      O
                   |      |
                   |      |
                   |     
                   -
                ''',
                # голова
                '''
                   --------
                   |      |
                   |      O
                   |    
                   |      
                   |     
                   -
                ''',
                # начальное состояние
                '''
                   --------
                   |      |
                   |      
                   |    
                   |      
                   |     
                   -
                '''
    ]
    return stages[tries]


def show_hint(th_w, th_w_comp):
    for i in range(len(th_w)):
        if th_w[i] != th_w_comp:
            if uniform(1, 2.5) <= 2:
                print("Попробуйте букву:", th_w[i])
            else:
                print("Попробуйте букву:", chr(ord('А')+randint(1, 25)))


def get_word():
    return choice(word_list).upper()


def play(word):
    print("Давайте играть в угадайку слов!")
    word_completion = ['_'] * len(word)  # строка, содержащая символы _ на каждую букву задуманного слова
    guessed = False  # сигнальная метка
    guessed_letters = []  # список уже названных букв
    guessed_words = []  # список уже названных слов
    tries = 6  # количество попыток
    print(display_hangman(tries))
    print(*word_completion, sep="")
    while not guessed and tries > 0:
        if tries <= 3:
            if word_completion[0] == "_" or word_completion[-1] == "_":
                word_completion[0] = word[0]
                word_completion[-1] = word[-1]
            else:
                show_hint(word_completion, word)
        st = input().upper()
        if st in guessed_letters or st in guessed_words or st.strip() == "":
            print(display_hangman(tries))
            print(*word_completion, sep="")
            continue
        if len(st) == 1:
            if st in word:
                for i in range(len(word)):
                    if word[i] == st:
                        word_completion[i] = st
                print(display_hangman(tries))
                print(*word_completion, sep="")
                if "_" not in word_completion:
                    guessed = True
            else:
                tries -= 1
                print(display_hangman(tries))
                print(*word_completion, sep="")
        else:
            guessed_words.append(st)
            if st == word:
                guessed = True
            else:
                tries -= 1
                print(display_hangman(tries))
                print(*word_completion, sep="")
        guessed_letters.append(st)
    if guessed:
        print("Поздравляем, вы угадали слово! Вы победили!")
    print("Слово было:", word)


n = "да"
while n.lower() != "нет, стоп, хватит, выйти, выход, конец, закончить" :
    play(get_word())
    print("Хотите поиграть еще?")
    n = input()

