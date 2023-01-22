def welcome_speech(t):
    print(f'''
    Добро пожаловать в игру - hangman 2000
    Ваша задача угадать загаданное слово за несколько попыток, 
    иначе вас ждет расплата!
    Загаданное слово состоит из {len(t)} букв {t}
    ''')


def start_template(w):
    return len(w)*['_']


def list_to_string_convert(t):
    s = ''
    for i in t:
        s += i
    return s


def user_input():
    return input('Введите букву: ')


def build_template(t, w, g=''):
    for i in range(len(w)):
        if w[i]== g:
            t[i] = g
    return t    


def get_word(w):
    return w[0]


def check_win(g):
    for i in g:
        if i == '_':
            return True
    return False


def check_mistake():




def game():
    progress = True
    word = ['orange']
    lifes = 3

    word_in_play = get_word(word)
    template = start_template(word_in_play)
    welcome_speech(list_to_string_convert(template))


    while progress:
        user_guess = user_input()
        template = build_template(template, word_in_play, user_guess)
        guessed = list_to_string_convert(template)
        print(f'Результат: {guessed}')
        progress = check_win(guessed)

        if not check_mistake(word_in_play, user_guess):




