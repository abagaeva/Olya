

from random import randint

game = True
num = randint(1, 100)

file = open('game_result', 'w', encoding = "utf8")

print('Попробуй угадать число от 1 до 100')
file.write('Попробуй угадать число от 1 до 100\n')

while game:
    guess = int(input('Ваше предложение:'))


    if guess == num:
        print('Вы угадали число!')
        file.write(f'Вы угадали число!{guess}\n')
        game = False
    elif guess < num:
        print('Вы не угадали число, загаданное число больше.Попробуйте еще раз')
        file.write(f'Вы не угадали число, загаданное число больше.Попробуйте еще раз.Ваше предположение {guess}\n')
    else:
        print('Вы не угадали, загаданное число меньше.Попробуйте еще раз.')
        file.write(f'Вы не угадали, загаданное число меньше.Попробуйте еще раз.Ваше предположение {guess}\n')
file.close()        
