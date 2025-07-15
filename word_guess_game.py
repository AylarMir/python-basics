word = input("Name a random word: ")
guess = ""
limit = 3
isAlive = True
i = 0
while guess != word and isAlive:
    if i < limit:
        guess = input("Guess the secret word: ")
        i += 1
    else:
        isAlive = False
if isAlive == False:
    print("Out of guesses. You lost!!")
else:
    print("Winner Winner!!")