def number(a):
    for i in range(a):
        print(str(i+1)*(i+1))

def user_input():
    return int(input('Введите число: '))

def c():
    o=user_input()
    number(o)

c()
