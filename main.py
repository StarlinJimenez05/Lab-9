def encode(password):
    _list = []
    for i in password:
        num = int(i)
        num = num + 3
        stringNum = str(num)
        _list.append(stringNum)
    s = ''
    result = s.join(_list)
    return result

def decode(password):
    list = []
    for i in password:
        num = int(i)
        num = num - 3
        stringNum = str(num)
        list.append(stringNum)
    s = ''
    string = s.join(list)
    return string

def main():
    while True:

        print('\nMenu')
        print('-------------')
        print('1. Encode')
        print('2. Decode')
        print('3. Quit')

        option = int(input('Please enter an option: '))

        if option == 1:
            password = input('Please input password to encode: ')
            savedPassword = encode(password)
            print('Your password has been encoded and stored!')
        if option == 2:
            print(f'The encoded password is {savedPassword}, and the original password is {password}')
        if option == 3:
            break

if __name__ == '__main__':
    main()