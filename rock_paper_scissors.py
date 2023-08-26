from random import choice

options = ('rock' , 'paper' , 'scissors')
player = input("choose between the options ('rock' , 'paper' , 'scissors') : ")
print(f'Player : {player}')
computer = choice(options)
print(f'Computer : {computer}')

def play():

    if player == 'rock' and computer == 'scissors':
        return 'you win'
    elif player == 'paper' and computer == 'rock':
        return 'you win'
    elif player == 'scissors' and computer == 'paper':
        return 'you win'
    elif player == 'rock' and computer == 'paper':
        return 'you lose'
    elif player == 'scissors' and computer == 'rock':
        return 'you lose'
    elif player == 'paper' and computer == 'scissors':
        return 'you lose'
    
while player == computer :
    print('It\'s a tie')
    player = input("choose between the options ('rock' , 'paper' , 'scissors') : ")
    print(f'Player : {player}')
    computer = choice(options)
    print(f'Computer : {computer}')

while player not in options :
    print('Error .')
    player = input("choose between the options ('sang' , 'kaghaz' , 'gheychi') : ")
    print(f'Player : {player}')
    computer = choice(options)
    print(f'Computer : {computer}')

print(play())

question = input('Do want to continue [y/n] :')

while question == 'y' :
    options = ('rock' , 'paper' , 'scissors')
    player = input("choose between the options ('rock' , 'paper' , 'scissors') : ")
    print(f'Player : {player}')
    computer = choice(options)
    print(f'Computer : {computer}')
    
    while player == computer :
        print('It\'s a tie')
        player = input("choose between the options ('rock' , 'paper' , 'scissors') : ")
        print(f'Player : {player}')
        computer = choice(options)
        print(f'Computer : {computer}')

    while player not in options :
        print('Error .')
        player = input("choose between the options ('rock' , 'paper' , 'scissors') : ")
        print(f'Player : {player}')
        computer = choice(options)
        print(f'Computer : {computer}')
    
    print(play())
    question = input('Do want to continue [y/n] :')
 
 
if question == 'n':
    print('Bye')
    