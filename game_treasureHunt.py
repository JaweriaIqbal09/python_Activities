from random import choice, randint
import os

class Player:
    def __init__(self, coin: int = 20, life: int = 3): 
        self.coins = coin
        self.lives = life
        self.party = []

    def add_coins(self, point):
        self.coins += point
        print("Coins:", self.coins)

    def lose_coins(self, point):
        if self.coins >= point:
            self.coins -= point
            print("Coins:", self.coins)
        else:
            print("Not enough coins!")

    def gain_life(self, lives=1):
        self.lives += lives
        print("Lives:", self.lives)

    def lose_life(self, lives=1):
        self.lives -= lives
        print("Lives:", self.lives)

    def check_win_condition(self):
        if self.coins >= 50 and "Warrior" in self.party:
            return True
            

    def check_lose_condition(self):
        if self.lives <= 0:
            return True

def data_text(location, decision, player):
    with open("D:\\gaming.txt", "a") as file:
        file.write(f"Location: {location}, Decision: {decision}, Coins: {player.coins}, Lives: {player.lives}\n")
def tavern(player):
    print("\nYou are in the Tavern.")
    print("1. Talk to Warrior")
    print("2. Go back to Village")

    ch = input("\nEnter your choice (1 or 2): ")
    if ch == "1":
        warrior_join = choice(["free", "cost"])
        if warrior_join == "free":
            print("Warrior joined your party for free!")
            player.party.append("Warrior")
            data_text("Tavern", "Warrior joined for free", player)
        else:
            if player.coins >= 10:
                player.lose_coins(10)
                player.party.append("Warrior")
                print("Warrior joined your party for 10 coins.")
                data_text("Tavern", "Warrior joined for 10 coins", player)
            else:
                print("Not enough coins to recruit the warrior.")
                data_text("Tavern", "Failed to recruit Warrior", player)
    elif ch == "2":
        data_text("Tavern", "Returned to Village", player)
        return "village"
    return "Tavern"


def forest(player):
    print("\nYou are in the Forest.")
    print("1. Open the Chest")
    print("2. Go back to Village")

    ch = input("Enter your choice (1 or 2): ")
    if ch == "1":
        result = choice(["coins", "trap"])
        if result == "coins":
            coins = randint(10, 30)
            player.add_coins(coins)
            print(f"You found {coins} coins in the chest.")
            data_text("Forest", f"Chest - gained {coins} coins", player)
        else:
            player.lose_life()
            print("You lost a life.")
            data_text("Forest", "Lost 1 life", player)
    elif ch == "2":
        data_text("Forest", "Returned to Village", player)
        return "village"
    return "forest"

def mountains(player):
    print("\nYou are in the Mountains.")
    print("1. Attempt to Climb")
    print("2. Go back to Village")

    ch = input("Enter your choice (1 or 2): ")
    if ch == "1":
        weather = choice(["sunny", "rain"])
        if weather == "sunny":
            coins = randint(15, 25)
            player.add_coins(coins)
            print(f"You earned {coins} coins.")
            data_text("Mountains", f"Sunny climb you earned {coins} coins", player)
        else:
            player.lose_life()
            print("It started raining! You slipped and lost a life.")
            data_text("Mountains", "Rainy climb - lost 1 life", player)
    elif ch == "2":
        data_text("Mountains", "Returned to Village", player)
        return "village"
    return "mountains"

def treasure_room(player):
    print("You entered the Treasure Room.")

    if player.check_win_condition():
        print("You have the Warrior and enough coins! You won the game!")
        data_text("Treasure Room", "Win", player)
        return "win"
    else:
        print("You need at least 50 coins and the Warrior in your party to win.")
        data_text("Treasure Room", "Failed to win", player)
        return "village"

def destination(player):
    print("\nYou are in the Village.")
    print("1. Go to Tavern")
    print("2. Go to Forest")
    print("3. Go to Mountains")
    print("4. Enter Treasure Room")

    ch = input("Enter your choice (1-4): ")
    if ch == "1":
        data_text("Village", "Go to Tavern", player)
        return tavern(player)
    elif ch == "2":
        data_text("Village", "Go to Forest", player)
        return forest(player)
    elif ch == "3":
        data_text("Village", "Go to Mountains", player)
        return mountains(player)
    elif ch == "4":
        data_text("Village", "Enter Treasure Room", player)
        return treasure_room(player)
    else:
        print("Invalid choice.")
        return "village"

def main():
    player = Player()
    location = "village"

    with open("gaming.txt", "w") as file:
        file.write("Game Started\n")

    print("\nWelcome to the Adventure Game!")
    print("You start with 20 coins and 3 lives.")

    while True:
        if player.check_lose_condition():
            print("Game Over! No lives left.")
            data_text(location, "Lost the Game", player)
            break

        if location == "village":
            location = destination(player)
        elif location == "Tavern":
            location = tavern(player)
        elif location == "forest":
            location = forest(player)
        elif location == "mountains":
            location = mountains(player)
        elif location == "Treasure Room":
            result = treasure_room(player)
            if result == "win":
                print("Congratulations! You finished the game.")
                break
            else:
                location = result

main()
