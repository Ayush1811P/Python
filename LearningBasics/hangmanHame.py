
import random
words = ["python", "yrogramming", "words", "jyush", "gaurav", "priyansh"]
lives = 6
print("Welcome to Hangman!")
while lives > 0:
    chosen_word = random.choice(words)
    guess = input("Guess a character: ").lower()
    if len(guess)!=1:
        print("enter one character only")
    
    if guess in chosen_word:
        
        print("Correct guess!\n Computer choice was: ",chosen_word)
        break
    else:
        lives -= 1
        print("_"*len(chosen_word))
        # print("computer chose: ",chosen_word)
        print(f"Wrong guess! Lives left: {lives}")

    if lives == 0:
        print(f"Game over! The word was: {chosen_word}")
        break







