import random

random = (random.randrange(1,10))
guessTime = 0

while True:
	try:
		guess = int(input("Guess the number(1-10): "))
		
		if guess < random:
			print("🔢your number is lower than the answer!")
			guessTime += 1
		elif guess > random:
			print("🔢your number is greater than the answer!")
			guessTime += 1
		else:
			guessTime += 1
			break
			
	except ValueError:
		print("🧐did you dont read my word before typing this?")
		guessTime += 1

print("🎉You won!!","|", "🐢you guess: ", guessTime)