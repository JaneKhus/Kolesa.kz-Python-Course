# 1
def getUserName():
    '''
    Gets Username.
    :return: FullName in a string format.
    '''
    return str(input('Type you full name.\n'))

def main():
    '''
    Greets user.
    :return: greetings
    '''
    fullName = getUserName()
    print("Добрый день, {0}, рады приветствовать вас!".format(fullName))

#main()

# 2
import numbers

def check_input(input):
    '''
    Method checks that input is a number.
    :param input:
    :return: True if variable is number.
    '''
    return isinstance(input, numbers.Number)


def getInput(tries = 0):
    '''
    Gets user input.
    :param tries: int параметр определяет текущую попытку ввода пользователя
    :return: Input number in a float format.
    '''
    if tries >= 3: return 'incorrect'
    inputNumber = float(input('Type your number:\n'))
    if not check_input(inputNumber) :
        tries += 1
        return getUserInput(tries)
    return inputNumber

def main2():
    '''
    Method formats input number.
    :return: 2 printed formats
    '''
    inputNumber = getInput()
    print('{:.2%}'.format(inputNumber), '\n')
    print('{:,}'.format(inputNumber), ' $\n')

main2()
