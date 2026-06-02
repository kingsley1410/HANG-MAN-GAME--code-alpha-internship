import random
words = ["king", "queen", "ruke", "bishop", "knight", "pawn"]
word = random.choice(words)
guessed_word = ["_"] * len(word)
chances = 6

print("Welcome to Hangman!")
print("Guess the chess word.")

while chances > 0:
    print("\nWord:", " ".join(guessed_word))
    print("Chances left:", chances)

    guess = input("Enter a letter: ").lower()

    if len(guess) != 1 or not guess.isalpha():
        print("Please enter a single letter.")
        continue

    if guess in word:
        print("Correct!")

        for i in range(len(word)):
            if word[i] == guess:
                guessed_word[i] = guess
    else:
        print("Wrong guess!")
        chances -= 1

    if "_" not in guessed_word:
        print("\n Congratulations! You guessed the word:", word)
        break

# If player loses
if "_" in guessed_word:
    print("\nGame Over!")
    print("The word was:", word)
