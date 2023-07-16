import random

from art import logo
from art import vs
from game_data import data
from utils import clear_terminal

score = 0

def compare_followers(person_a, person_b):
    if person_a['follower_count'] > person_b['follower_count']:
        return 'a'
    else:
        return 'b'

# Game logic ------------------------------------------------------------
guessed_right = True
while True:
    clear_terminal()
# Print logo
    print(logo)
    if guessed_right:
        if score > 0:
            print(f"You are right. Your score {score}")
# Pick a person A
        person_a = random.choice(data)
# Pick a person B != person A
        while True:
            person_b = random.choice(data)
            if person_a != person_b:
                break
# Print person A, vs, person B
        print(f"Compare A: {person_a['name']}, {person_a['description']}, from {person_a['country']}")
        print(vs)
        print(f"Against B: {person_b['name']}, {person_b['description']}, from {person_b['country']}")
# Ask a player to choose who has more followers
        choice = input("Who has more followers? Type 'A' or 'B': > ").lower()
# Compare player's input with correct answer
# Increase score if a player guessed right or end a game if they was wrong
        if compare_followers(person_a, person_b) != choice:
            guessed_right = False
        else:
            score += 1 
    else:
        print(f"Sorry, you are wrong. Your final score is {score}")
        break
