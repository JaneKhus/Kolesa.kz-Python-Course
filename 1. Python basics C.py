import math
import numbers

def check_input(input):
    '''
    Method checks that input is a number.
    :param input:
    :return: True if variable is number.
    '''
    return isinstance(input, numbers.Number)

def getUserInput(tries = 0):
    '''
    Method collects valid user's input

    :param tries: int параметр определяет текущую попытку ввода пользователя
    :return: str вариант пути пользователя 'radius' | 'diametr' | 'incorrect'
    '''
    if tries >= 3: return 'incorrect'

    coefficientA = int(input('This program solves equations like a * X^2 + b * X + c = 0. \nType A:\n '))
    if not check_input(coefficientA) :
        tries += 1
        return getUserInput(tries)

    coefficientB = int(input('Type B:\n '))
    if not check_input(coefficientB) :
        tries += 1
        return getUserInput(tries)

    coefficientC = int(input('Type C:\n '))
    if not check_input(coefficientC):
        tries += 1
        return getUserInput(tries)

    coefficients = [coefficientA, coefficientB, coefficientC]
    return coefficients

def getEquationRootes(coefficients):
    '''
    Method prints equations roots.
    '''
    if coefficients[1]**2 - 4 * coefficients[0] * coefficients[2] >= 0:
        print('X1: ', (-coefficients[1] - math.sqrt(coefficients[1]**2 - 4 * coefficients[0] * coefficients[2]))/ (2 * coefficients[0]), '\n')
        print('X2: ', (-coefficients[1] + math.sqrt(coefficients[1]** 2 - 4 * coefficients[0] * coefficients[2])) / (2 * coefficients[0]), '\n')
    else:
        print('b^2 - 4ac should be bigger than 0\n')

def main():
    '''
    Method returns quadratic equations root.

    :return: void
    '''

    coefficients = getUserInput()
    if coefficients == 'incorrect' : print("You entered wrong input.")
    print("Equation is {0} * X^2 + {1} * X + {2} = 0".format(coefficients[0], coefficients[1], coefficients[2]))

    getEquationRootes(coefficients)

main()