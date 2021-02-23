import random
from hangman_art import stages,logo
from hangman_words import word_list
from replit import clear

chosen_word = random.choice(word_list)
word_length = len(chosen_word)
end_of_game = False
lives = 6
print(logo)

print(f"the chosen word is {chosen_word}")

#Create blanks
display = []
for _ in range(word_length):
  display += "_"

while not end_of_game:

  guess = input("Guess the letter:").lower()

  clear()

  if guess in display:
    print(f"You have already guessed letter {guess}")
  
  #check the guess letter:

  for position in range(word_length):
    letter = chosen_word[position]
    if letter == guess:
      display[position] = letter
  print(f"{' '.join(display)}")
  
  #check if user is wrong
  if guess not in chosen_word:
    print(f"The guess letter {guess} is not in the chosen word. You loose a life")
    lives -= 1
    if lives == 0:
      end_of_game = True
      print("You lose")
  
  #check if  user is right
  if "_" not in display:
    end_of_game = True
    print("You win")
  
  print(stages[lives])
  
  
    









