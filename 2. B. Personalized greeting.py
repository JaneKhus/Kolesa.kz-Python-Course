from prettytable import PrettyTable

def getUserData():
    '''
    Asks for user data.
    :return: list of userFirstName, userLastName, userAge, userAddress, userTelephone.
    '''
    userFirstName = str(input('Type your first name.\n'))
    userLastName = str(input('Type your last name.\n'))
    userAge = int(input('Type your age.\n'))
    userAddress = str(input('Type your address.\n'))
    userTelephone = str(input('Type your telephone.\n'))
    isFemale = str(input('Type 1 if you\'re Female, else 0.\n'))
    return [userFirstName, userLastName, userAge, userAddress, userTelephone, isFemale]

def prettifyData(list):
    """
    Prints pretty data.
    :param list:
    :return:
    """
    Table = PrettyTable()
    Table.field_names = ["First name", "Last name", "Age", "Address", "Telephone", "Gender"]
    Table.add_row(list)
    print(Table)

def main():
    '''
    Method prints user data.
    :return: table
    '''
    table = getUserData()
    prettifyData(table)


def getPersonalizedGreeting(userAge, isFemale, userFirstName, userLastName):
    if isFemale == 1 & userAge < 18:
        print('Гоу ботать, {0}'.format(userFirstName))
    if userAge >= 18:
        print('Гоу работать, {0} {1}'.format(userFirstName, userLastName))
    if isFemale == 0 & userAge < 18:
        print('Бери мороженку в холодильнике, {0}'.format(userFirstName))


def main2 ():
    table = getUserData()
    getPersonalizedGreeting(table[2], table[-1], table[0], table[1])


main2()