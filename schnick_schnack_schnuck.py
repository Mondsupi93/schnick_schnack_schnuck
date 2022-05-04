import random
from tokenize import Name

user_win_counter = 0
player_win_counter = 0

print(      'rock...paper...scissor'      )

name = input('Please enter your name : ')
lap = int(input('please return lap ? '))

for num in range(1, lap+1):
    
    user = input('Please return your choise ? ')   

    number = random.randint(1,3)

    player = ''
  
    if number == 1:
        player= 'rock'
        print('player choise rock')
    
    elif number == 2:
        player = 'paper'
        print('player choise paper')
    
    elif number == 3:
        player = 'scissor'
        print('player choise scissor')

    
    if player == 'rock' and user == 'paper':
        print(name ,'win')
        user_win_counter += 1
    
    elif player == 'rock' and user == 'scissor':
        print('player win')
        player_win_counter += 1
    
    elif player == 'paper' and user == 'rock':
        print('palyer win')
        player_win_counter += 1
    
    elif player == 'paper' and user == 'scissor':
        print(name ,'win')
        user_win_counter += 1
    
    elif player == 'scissor' and user == 'paper':
        print('palyer win')
        player_win_counter += 1
    
    elif player == 'scissor' and user == 'rock':
        print(name ,'win')
        user_win_counter += 1
    
    else:
        print('No one won the match!!!')
    
print(name, user_win_counter, 'won the match and player',player_win_counter, 'won the match' )

        
