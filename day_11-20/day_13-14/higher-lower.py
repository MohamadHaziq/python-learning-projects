## Higher-Lower game

import random
import game_data
import art 
import os

def clear(): 
      # for windows 
    if os.name == 'nt': 
        _ = os.system('cls') 
  
    # for mac and linux(here, os.name is 'posix') 
    else: 
        _ = os.system('clear') 

data = game_data.data

def check_answer(choice1, choice2):
    answer = ''
    if choice1['follower_count'] > choice2['follower_count']:
        answer = 'a'
    if choice1['follower_count'] < choice2['follower_count']:
        answer ='b'
    return answer
    
def versus(choice1, choice2):
    print("Game on guys ! Who has more followers ?")
    print('')
    print(f"Compare A: {choice1['name']}: A {choice1['description']} from {choice1['country']}")
    print(art.vs)
    print(f"Against B: {choice2['name']}: A {choice2['description']} from {choice2['country']}")
    print('')


def play_higher_lower():
    option_a = random.choice(data)
    option_b = random.choice(data)

    current_score = 0
    print(art.logo)

    cont_game = True
    while cont_game:
        versus(option_a,option_b)
        answer = check_answer(option_a, option_b)
        
        choice = input("Who has more followers ? 'A' or 'B'?: ").lower()
        
        clear()

        if choice == answer:
            current_score += 1
            option_a = option_b
            option_b = random.choice(data)
            print (f'You got it right ! Current score is {current_score} \n')
            
        else:
            print(art.logo)
            print ('Too bad, you lost.')
            print(f'Your final score is {current_score} \n')
            cont_game = False

# play = input("Do you want to play the game ? 'y' or 'n': ")
play_higher_lower()

# print(option_a)
# print(option_b)