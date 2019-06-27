import time

count = 10

welcome = 'Bienvenido al Timer. T-10SEG'

def _timer():
    global count
    while count > 0:
        time.sleep(1)
        print(count)
        count -= 1


if __name__ == '__main__':
    print(welcome)
    print(_timer())