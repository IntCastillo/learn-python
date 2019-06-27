
name = 'cristian'

# Get the name & greating
def get_name(username):
    global name

    if username not in name:
        name += username
        print('Thanks for sign in!')
    else:
     print('Ups! username is already taken :(')

# Welcome to the user
def _print_welcome():
    print('Welcome, user!')
    return('*' * 14)

# All user registered
def all_users():
    global name
print(name)

if __name__ == '__main__':

    print(_print_welcome())
    username = input('Enter your name:')
    get_name(username)
    print(all_users())



  