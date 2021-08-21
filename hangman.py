import random

print("""H A N G M A N
The game will be available soon.""")

words = 'python', 'java', 'kotlin', 'javascript'
game_word = random.choice(words)

tip = game_word[0:3] + ("-" * (len(game_word) - 3))

word = input(f"Guess the word {tip} : ")

if word == game_word:
    print("You survived!")
else:
    print("You lost!")
