import random

# Predefined list of words
words = ["apple", "grape", "mango", "peach", "melon"]

# Choose a random word
word_to_guess = random.choice(words)
guessed_word = ["_"] * len(word_to_guess)
guessed_letters = []
max_attempts = 6
attempts = 0

print("🎯 Welcome to Hangman!")
print("Guess the word:", " ".join(guessed_word))

while attempts < max_attempts and "_" in guessed_word:
    guess = input("Enter a letter: ").lower()

    if not guess.isalpha() or len(guess) != 1:
        print("⚠️ Please enter a single valid letter.")
        continue

    if guess in guessed_letters:
        print("🔁 You already guessed that letter.")
        continue

    guessed_letters.append(guess)

    if guess in word_to_guess:
        print("✅ Good guess!")
        for i, letter in enumerate(word_to_guess):
            if letter == guess:
                guessed_word[i] = guess
    else:
        print("❌ Wrong guess!")
        attempts += 1

    print("\nWord:", " ".join(guessed_word))
    print(f"Remaining attempts: {max_attempts - attempts}")
    print("Guessed letters:", ", ".join(guessed_letters))
    print("-" * 30)

# Game result
if "_" not in guessed_word:
    print("🎉 Congratulations! You guessed the word:", word_to_guess)
else:
    print("💀 Game over! The word was:", word_to_guess)
