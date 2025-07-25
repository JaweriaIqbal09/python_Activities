POINTS = {
    'A': 1, 'B': 3, 'C': 3, 'D': 2, 'E': 1, 'F': 4,
    'G': 2, 'H': 4, 'I': 1, 'J': 8, 'K': 5, 'L': 1,
    'M': 3, 'N': 1, 'O': 1, 'P': 3, 'Q': 10, 'R': 1,
    'S': 1, 'T': 1, 'U': 1, 'V': 4, 'W': 4, 'X': 8,
    'Y': 4, 'Z': 10
}

def compute_score(word):
    total = 0
    for letter in word.upper():
        points = POINTS.get(letter, 0)
        total += points
    return total

x = input("Enter Player 1 name : ")
y = input("Enter Player 2 name : ")

rounds = int(input("Number of rounds to play: "))

total_score1 = 0
total_score2 = 0

highest_score1 = 0
highest_score2 = 0

longest_word1 = 0
longest_word2 = 0

for i in range(1, rounds + 1):
    print("\n--- Round", i, "---")
    player1 = input(f"{x.upper()}'s turn : ")
    player2 = input(f"{y.upper()}'s turn : ")

    score_1 = compute_score(player1)
    score_2 = compute_score(player2)

    print("Scores:\n", x.upper(), "=", score_1, "\n", y, "=", score_2)

    total_score1 += score_1
    total_score2 += score_2

    if score_1 > highest_score1:
        highest_score1 = score_1
    elif score_2 > highest_score2:
        highest_score2 = score_2

    if len(player1) > longest_word1:
        longest_word1 = len(player1)
    elif len(player2) > longest_word2:
        longest_word2 = len(player2)

    if score_1 > score_2:
        print(x.upper(), "wins this round!")
    elif score_2 > score_1:
        print(y.upper(), "wins this round!")
    else:
        print("This round is a tie!")

print("\n=== Final Tournament Results ===")
print(x.upper() , ": Total =", total_score1, ", Highest =", highest_score1, ", Longest =", longest_word1)
print(y.upper() , ": Total =", total_score2, ", Highest =", highest_score2, ", Longest =", longest_word2)

if total_score1 > total_score2:
    print("\n" + x.upper() + " wins the tournament!")
elif total_score2 > total_score1:
    print("\n" + y.upper() + " wins the tournament!")
else:
    if highest_score1 > highest_score2:
        print("\n" + x.upper() + " wins the tournament by highest scoring word!")
    elif highest_score2 > highest_score1:
        print("\n" + y.upper() + " wins the tournament by highest scoring word!")
    else:
        if longest_word1 > longest_word2:
            print("\n" + x.upper() + " wins the tournament by longest word!")
        elif longest_word2 > longest_word1:
            print("\n" + y.upper() + " wins the tournament by longest word!")
        else:
            print("\nThe tournament is complete tie!")
