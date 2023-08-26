import random

computer = random.randint(1 , 50)
player = ''

while player != computer :
    player = int(input('Enter a number between 1 to 50 : '))

    if player < computer :
        print('Mine is bigger')
    elif player > computer :
        print('Mine is smaller')
print(computer)
print('You win!!!!!')