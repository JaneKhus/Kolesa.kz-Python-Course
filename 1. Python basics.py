#A: Реализуйте при помощи python формулу длинны окружности через радиус или диаметр. L=2πr или L=πD.

import math
pi = math.pi

def check_input(input):
    if input > 0:
        return "Ok"
    else:
        return "Not ok"

def circle_length_r(radius):
    length = 2 * pi * radius
    return length

def circle_length_d(diameter):
    length = pi * diameter
    return length

def choose_method(type):
    if type == 1:
        radius = int(input('Введите радиус \n'))
        if check_input(radius) == "Ok":
            return circle_length_r(radius)
        else:
            return "Number should be bigger than 0"
    if type == 2:
        diameter = int(input('Введите диаметр \n'))
        if check_input(diameter) == "Ok":
            return circle_length_r(diameter)
        else:
            return "Number should be bigger than 0"
    else:
        print('Wrong number. Type 1 or 2')


def main():
    user_response = 1
    while user_response == 1:
        print('Type 1 if you know radius. \nType 2 if you know diameter.\n ')
        type = int(input('\n '))
        result = choose_method(type)
        print(result)
        print('Continue? 1 = Yes, Other number = No \n')
        user_response = int(input('\n '))

main()