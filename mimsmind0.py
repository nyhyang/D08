# In the 'mimsmind' game, the computer program 
# will generate a random integer number and prompt the human player to guess the number. 
# After each guess, the computer will 
# provide feedback to guide the human in making his/her next guess. 
# The game will end when the player correctly guesses the number 
# or when the player runs out of guesses.

# We would like you to implement this game in two versions. 
# You should complete version 0 before starting on version 1.


# In this version, the program generates a random number with number of digits equal to length.
# If the command line argument length is not provided, the default value is 1. 
# Then, the program prompts the user to type in a guess, 
# informing the user of the number of digits expected. 
# The program will then read the user input, and provide basic feedback to the user. 
# If the guess is correct, 
# the program will print a congratulatory message with the number of guesses made and terminate the game. 
# Otherwise, the program will print a message asking the user to guess a higher or lower number, 
# and prompt the user to type in the next guess.

import random 

def number_guessing():
	print("Let's play the mimsmind0 game.")
	answer = input("Please enter the digit of number you are interested in guessing: ")
	if answer == "":
		answer = 1
	else:
		answer = int(answer)
	# to finalize the digit using from user input 
	random_interger = random.randint(1, (10 ** answer)+1)

	count = 0
	while True:
		count += 1
		user_guess = int(input("Please take guess a {} digit numer: ".format(answer)))
		if user_guess == random_interger:
			print("Congratulations. You guessed the correct number in {} times.".format(count))
			break	
		elif user_guess < random_interger:
			print("Try again. Guess a higher number:")
			
		else:
			print("Try again. Guess a lower number:")
			

# not sure how to do infinite count during the try and error. 
# I'm thinking to intialize a var = 0. 
# As the counts cotinue += var
# Add to Congrats ... with the .format() 
# but not sure how to add up


def main():

	number_guessing()

if __name__ == '__main__':
	main()