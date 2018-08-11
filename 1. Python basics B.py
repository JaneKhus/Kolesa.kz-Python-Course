#Реализуйте при помощи python и библиотеки math (import math) формулу длины  окружности через площадь круга. L= 2√(s*π)

import math
pi = math.pi

def circle_length():
    area = int(input('\n '))
    if area > 0:
        length = 2 * math.sqrt(math.pi * area)
        return length
    else:
        return "Number should be bigger than 0"

def main():
    print('Type area of circle:')
    result = circle_length()
    print(result)

main()
