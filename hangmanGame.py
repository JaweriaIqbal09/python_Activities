import random

print("Welcome to HangGame!")

# Word list
words = ["apple", "banana", "orange", "grapes", "mango"]

# Get a random word from the list
rand_index = random.randint(0,4)
selected_word = words[rand_index]

# Store guessed letters and score
guessed_letters = []
score = 0

# Ask user to guess letters
while True:
    print("Word : ",len(selected_word)*"_ ")
    user_input = input("Guess a letter: ").lower()

    # Check if already guessed
    if user_input in guessed_letters:
        print("You have guessed that earlier before.")
        print("Score:", score)
        continue

    guessed_letters.append(user_input)

    # Check if letter is in the word
    if user_input in selected_word:
        print("✅ Good job! You guessed correctly.")
        score += 1
    else:
        print("❌ Wrong guess.")
        score -= 1

    print("Score:", score)

    # Check if all letters guessed
    all_found = True
    for letter in selected_word:
        if letter not in guessed_letters:
            all_found = False
            break

    if all_found:
        print("🏁Congratulations 🎉 ! You guessed the word:", selected_word)
        print("Final Score:", score)
        break

