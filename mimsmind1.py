
# A matching digit in the correct position will result in a 'bull', 
# while a matching digit in the wrong position will result in a 'cow'. 
# For example, if the correct answer is '123', and the guess is '324', 
# then the feedback will be one bull (for the digit '2') 
# and one cow (for the digit '3'). More examples are provided below.

# At each round, 
# if the user guess is incorrect and maxrounds is not yet reached, 
# the program should increment the counter for round 
# and issue a new prompt for user input. 
# Otherwise, the program should print a congratulatory 
# or an apologetic message with the number of guesses made, 
# and terminate the game.

import random 

def number_guessing():
	print("Let's play the mimsmind0 game.")
	answer = int(input("Please enter the digit of number you are interested in guessing: "))
	if answer == "":
		answer = 3
	# else:
	# 	answer = int(answer)
	random_interger = random.randint(0, (10 ** answer))
	final_answer = str(random_interger)
	if len(final_answer) < 3:
		final_answer = (3 - len(final_answer) * 0) + final_answer
	return final_answer
	
	maxrounds = (2 ** answer) + answer
	print("You have {} guesses.".format(maxrounds))

	while maxrounds > 0:
		user_guess = input("Please take guess a {} digit numer: ".format(answer))
		lst_randint = list(final_answer)
		lst_userguess = list(user_guess)
		
		bulls = 0
		cows = 0
		for c, d in zip(lst_randint, lst_userguess):
			if c == d:
				bulls += 1
			else:
				if d in lst_randint and d in lst_userguess:
					cows += 1
			maxrounds -= 1
		print("{} bull(s), {} cow(s)".format(bulls, cows))
		if bulls == len(answer):
			print("Congratulations! You guessed the correct number in {} times".format((2 ** len(answer) + len(answer)) - user_guessleft)







def main():
	
	number_guessing()

if __name__ == '__main__':
	main()