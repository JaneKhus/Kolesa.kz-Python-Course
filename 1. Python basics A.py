#A: Реализуйте при помощи python формулу длинны окружности через радиус или диаметр. L=2πr или L=πD.

import math
pi = math.pi

def check_input(input):
    return  input > 0

def get_circle_length_r(radius):
    return 2 * pi * radius

def get_circle_length_d(diameter):
    return pi * diameter


def getUserChoice(tries = 0):
    '''
    метод возвращает способ решения задачи выбранный пользователем

    :param tries: int параметр определяет текущую попытку ввода пользователя
    :return: str вариант пути пользователя 'radius' | 'diametr' | 'incorrect'
    '''

    userChoice = int(input('Type 1 if you know radius. \nType 2 if you know diameter.\n '))

    if 1 == userChoice : return 'radius'

    if 2 == userChoice : return 'diametr'

    tries +=1

    if tries >= 3 : return 'incorrect'

    return getUserChoice(tries)


def runRadiusWay():
    '''
    метод выплняет логику нахождения длинны окружности по радиусу
    '''
    radius = float(input("Введите радиус:\n"))

    if check_input(radius):
        print (get_circle_length_r(radius))
    else:
        print('Вы ввели неверно радиус')


def runDiametrWay():
    '''
    метод выполняет логику нахождения длинны окружности по диаметру
    '''
    diametr = float(input("Введите диаметр:\n"))

    if check_input(diametr):
        print (get_circle_length_r(diametr))
    else:
        print('вы ввели неверно диаметр')


def main():
    '''
    Метод реализует формулу длинны окружности через радиус или диаметр. L=2πr или L=πD.

    :return: void
    '''

    userWay = getUserChoice()

    if userWay == 'incorrect' : print("вы не выбрали способ решения задачи")

    if userWay == 'radius' : runRadiusWay()

    if userWay == 'diametr' : runDiametrWay()



main()