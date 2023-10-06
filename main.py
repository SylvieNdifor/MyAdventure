class Character:
    def __init__(self, name):
        self.name = name


class Game:
    def __init__(self):
        self.player = Character("You")
        self.love_interest = Character("Your Crush")
        self.romance_level = 0

    def flirt(self):
        if self.romance_level < 2:
            print(f"You blush and flirt with {self.love_interest.name}.")
            print(f"{self.love_interest.name} smiles in response.")
        elif self.romance_level == 2:
            print(f"You flirt with {self.love_interest.name} and hold their hand.")
            print(f"{self.love_interest.name} blushes and squeezes your hand.")

    def compliment(self):
        if self.romance_level < 2:
            print(f"You pay a compliment to {self.love_interest.name}.")
            print(f"{self.love_interest.name} blushes and thanks you.")
        elif self.romance_level == 2:
            print(f"You give a heartfelt compliment to {self.love_interest.name}.")
            print(f"{self.love_interest.name} smiles warmly and leans closer to you.")

    def gift(self):
        if self.romance_level < 2:
            print(f"You give a small gift to {self.love_interest.name}.")
            print(f"{self.love_interest.name} is touched by your gesture.")
        elif self.romance_level == 2:
            print(f"You surprise {self.love_interest.name} with a thoughtful gift.")
            print(f"{self.love_interest.name} hugs you tightly and whispers, 'I love it!'")


def romantic_adventure():
    game = Game()

    print("Welcome to the Romantic Adventure Game!")
    print(f"You are deeply in love with {game.love_interest.name}.")

    while True:
        print("\nWhat would you like to do?")
        print("1. Flirt")
        print("2. Compliment")
        print("3. Gift")
        print("4. Quit")

        choice = input("Enter your choice (1/2/3/4): ")

        if choice == "1":
            game.flirt()
            game.romance_level += 1
        elif choice == "2":
            game.compliment()
            game.romance_level += 1
        elif choice == "3":
            game.gift()
            game.romance_level += 1
        elif choice == "4":
            print(f"{game.love_interest.name} smiles and says goodbye.")
            break
        else:
            print("Invalid choice. Please select a valid option.")


if __name__ == "__main__":
    romantic_adventure()
