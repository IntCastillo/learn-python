count = 100


def _cuenta_regresiva():
       global count
       while count > 0:
          print(count)
          count -=1


if __name__ == '__main__':
    print(_cuenta_regresiva())