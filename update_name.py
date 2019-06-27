
name = 'cristian'


def welcome():
    print('Welcome, you can change your name')
    print('*' * 10)

def get_name():
    global name
    print('Tu nombre actual', name)


if __name__ == '__main__':
    print(welcome())

    get_name = input('Enter your actual name: ')
    print(get_name())