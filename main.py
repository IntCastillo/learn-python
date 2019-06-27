clients = 'pablo,ricardo,'

# Create client

def create_client(client_name):
    global clients

    if client_name not in clients:
        clients += client_name
        _add_comma()
    else:
        print('Client already is in the client\'s list')

# List name in list client
def list_clients():
    global clients

    print(clients)

def update_client(client_name, updated_client_name):
    global clients

    if client_name in clients:
        clients = clients.replace(client_name + ',', updated_client_name)
    else:
        print('Client is not in clients list')

# [S]earch Command. Itera sobre los nombres de los clientes
def search_client(client_name):
    list_clients = clients.split(',')

    for client in list_clients:
        if client != client_name:
            continue
        else:
            return True


# Add comma after every name in clients variable

def _add_comma():
    global clients

    clients += ','

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
    return input('What is the cliente name? ')

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
        pass #Investigar este punto
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