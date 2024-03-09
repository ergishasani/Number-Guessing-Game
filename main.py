import random
from art import logo

EASY_LEVEL_TURNS = 10
HARD_LEVEL_TURNS =  5

#Function to check the user's guess againts the actual guess
def check_answear(guess, answer, turns):
    if guess > answer:
        print("Too high.")
        return turns - 1
    elif guess < answer:
        print("Too low.")
        return  turns - 1
    else:
        print(f"You got it! The answear was {answer}.")

#Function for the dificulty of the game
def set_dificulty():
    level =  input("Choose the difficulty. Type 'easy' or 'hard': ").lower()
    if level == "easy":
        return  EASY_LEVEL_TURNS
    else:
        return HARD_LEVEL_TURNS

#Game function
def game():
    print(logo)
    #Choosing a random number between 1 and 100.
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")
    answer = random.randint(1, 100)
    print(f"Pssst, the correct answer is {answer}") 
    
    turns = set_dificulty()
    #While loop to check the turns
    guess = 0
    while guess != answer:
        print(f"You have {turns} attemps remaining to guess the number.")
        
        guess = int(input("Make your guess: "))
        
        turns=check_answear(guess, answer, turns)
        if turns==0:
            print("You've run out of guesses, you lose.")
            return
        elif guess != answer:
            print("Guess Again!")

game()