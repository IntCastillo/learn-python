import time
# Última letra del nombre

# Definir función que guarda el valor

def Welcome():
    print('*' * 10)
    print('Bienvenido!')
    print('*' * 10)
    pass


# Obtener el nombre
def getName():
    print('La última letra de tu nombre es', username[-1])

# Iniciar el programa

if __name__ == '__main__':
    print(Welcome())
    username = input('Cuál es tu nombre? ')
    time.sleep(.3)
    print(getName())