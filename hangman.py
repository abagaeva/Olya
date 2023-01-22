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
    pass
def get_word(w):
    return w[0]
    









def game():
    progress = True
    word = ['orange']
    lifes = 3

    word_in_play = get_word(word)
    template = start_template(word_in_play)
    welcome_speech(list_to_string_convert(template))
    