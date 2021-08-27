import random

print("H A N G M A N")

words = 'python', 'java', 'kotlin', 'javascript'
game_word = random.choice(words)
tip = len(game_word) * "-"
x = 0

while x < 8:
    print("")
    print(tip)
    # print(game_word)
    carta = input("Input a letter: ")
    if carta in game_word:
        tip = list(tip)
        for id, letter in enumerate(game_word):
            if carta == letter:
                tip[id] = carta
                # print(id)
        tip = "".join(tip)
    else:
        print("That letter doesn't appear in the word")
    x += 1

print("""
Thanks for playing!
We'll see how well you did in the next stage""")
