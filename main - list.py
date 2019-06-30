import sys

clients = ['pablo', 'ricardo']

# Create client

def create_client(client_name):
    global clients

    if client_name not in clients:
        clients.append(client_name) # Concatenación de strings es modificado por el método (append)
    else:
        print('Client already is in the client\'s list')

# List name in list client
def list_clients():
    for idx, client in enumerate(clients): # Hacemos uso de la función enumerate para conocer el índice del cliente
        print('{}: {}'.format(idx, client)) # Formateamos con placeholders para que pase el índice con su respectivo client_name


def update_client(client_name, updated_client_name):
    global clients

    if client_name in clients:
        index = clients.index(client_name)
        clients[index] = update_client_name
    else:
        print('Client is not in clients list')

# [D]elete Command. Toma el client_name y lo elimina dentro de clients

def delete_client(client_name):
    global clients

    if client_name in clients:
        clients.remove(client_name)
    else:
        print('Client is not in the client\'s list')


# [S]earch Command. Itera sobre los nombres de los clientes
def search_client(client_name):
    for client in clients:
        if client != client_name:
            continue
        else:
            return True


# Print all the welcome message

def _print_welcome():
    print('Welcome to PlatziVentas')
    print('*' * 50)
    print('What do you like to do today? ')
    print('[C]reate client')
    print('[L]ist clients')
    print('[U]pdate client')
    print('[D]elete client')
    print('[S]earch client')

# Private method (maybe why use return keyword). 
# i'll be reused in other functions

def _get_client_name():
    return input('What is the client name? ')

# Main method that print the program

if __name__ == '__main__':
    _print_welcome()

    command = input()
    command = command.upper()

    if command == 'C':
        client_name = _get_client_name()
        create_client(client_name)
        list_clients()
    elif command == 'D':
        client_name = _get_client_name()
        delete_client(client_name)
        list_clients()
    elif command == 'L':
        list_clients()
    elif command == 'U':
        client_name = _get_client_name()
        update_client_name = input('What is the updated client name? ')
        update_client(client_name, update_client_name)
        list_clients()

    elif command == 'S':
        client_name = _get_client_name()
        found = search_client(client_name)
    
        if found:
           print('The client is in the client\'s list')
        else:
           print('The client: {} is not in our client\'s list'.format(client_name))
    else:
        print('Invalid command')