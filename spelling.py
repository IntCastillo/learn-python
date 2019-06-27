import time
import datetime


sentences = 'John'


def _number_of_letters():
    print('Tu nombre tiene', len(sentences), 'caracteres')

def _spell_():
    for sentence in sentences:
        time.sleep(1)
        print('Current Letter', sentence)
        

    print('Deletreo terminado!')

def time_is():
 current_time = datetime.datetime.now()

 print('La hora en la que haz iniciado es: ', str(current_time.hour))
 

if __name__ == '__main__':
    print(time_is())
    time.sleep(3)
    _spell_()
    time.sleep(3)
    _number_of_letters()
    print('it\'s works! Thanks god.')