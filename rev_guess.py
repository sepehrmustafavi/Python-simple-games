import random

player = int(input('Enter a number between 1 - 100 : '))
computer = ''

kaf = 1
saghf = 100
while computer != player :
    computer = random.randint(kaf + 1, saghf - 1)
    print(computer)

    if computer < player :
        print('Mine is bigger .')
        kaf = computer

    elif computer > player :
        print('Mine is smaller .')
        saghf = computer

print('you won!!!!')