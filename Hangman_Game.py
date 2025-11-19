import random

# -----------------------------------------------------------
#  Hangman Game (Python Console Version)
#  Uses OOP principles, input validation, ASCII visuals,
#  and a replayable game loop.
# -----------------------------------------------------------

class Hangman:
    def __init__(self, word_list, max_attempts=6):
        """Initialize the game with a random word and counters."""
        self.word = random.choice(word_list).lower()  # Pick a random word
        self.guessed_letters = []                    # Store correct guesses
        self.wrong_guesses = []                      # Store wrong guesses
        self.max_attempts = max_attempts             # Allowed wrong attempts
        self.attempts_left = max_attempts            # Remaining attempts

    def display_word(self):
        """Show the word with underscores for unguessed letters."""
        display = ""
        for letter in self.word:
            if letter in self.guessed_letters:
                display += letter + " "
            else:
                display += "_ "
        return display.strip()

    def guess(self, letter):
        """Handle a user's guess."""
        
        # Validate input
        if not (len(letter) == 1 and letter.isalpha()):
            print("❌ Invalid input! Enter a single letter.\n")
            return
        
        # Prevent duplicate guesses
        if letter in self.guessed_letters or letter in self.wrong_guesses:
            print("⚠️ Already guessed!\n")
            return
        
        # Check if guess is correct
        if letter in self.word:
            print("✅ Correct guess!\n")
            self.guessed_letters.append(letter)
        else:
            print("❌ Wrong guess!\n")
            self.wrong_guesses.append(letter)
            self.attempts_left -= 1

    def is_won(self):
        """Check if the player has guessed all letters."""
        return all(letter in self.guessed_letters for letter in self.word)

    def is_lost(self):
        """Check if the player has no attempts left."""
        return self.attempts_left <= 0
    
    def display_hangman(self):
        """Return ASCII art depending on the number of wrong guesses."""
        stages = [
            """
               ------
               |    |
               |
               |
               |
               |
            """,
            """
               ------
               |    |
               |    O
               |
               |
               |
            """,
            """
               ------
               |    |
               |    O
               |    |
               |
               |
            """,
            """
               ------
               |    |
               |    O
               |   /|
               |
               |
            """,
            """
               ------
               |    |
               |    O
               |   /|\\
               |
               |
            """,
            """
               ------
               |    |
               |    O
               |   /|\\
               |   /
               |
            """,
            """
               ------
               |    |
               |    O
               |   /|\\
               |   / \\
               |
            """    
        ]
        
        # wrong attempts = max_attempts - attempts_left
        wrong_attempts = self.max_attempts - self.attempts_left
        return stages[wrong_attempts]
    
    def print_status(self):
        """Print the hangman, current word state, and guesses."""
        print(self.display_hangman())
        print("Word:", self.display_word())
        print("Correct guesses:", ', '.join(self.guessed_letters) if self.guessed_letters else "None")
        print("Wrong guesses:", ', '.join(self.wrong_guesses) if self.wrong_guesses else "None")
        print("Attempts left:", self.attempts_left, "\n")

    def play(self):
        """Main game loop."""
        print("🎉 Welcome to Hangman! 🎉")
        print("\nYour word contains", len(self.word), "letters.\n")
        
        while not self.is_won() and not self.is_lost():
            self.print_status()
            guess = input("Enter a letter: ").lower()
            self.guess(guess)
            
        # Game end
        if self.is_won():
            print("\n🎉 You won! The word was:", self.word)
        else:
            print(self.display_hangman())
            print("\n💀 You lost! The word was:", self.word)


# ---------------- MAIN GAME LOOP ----------------
if __name__ == "__main__":
    words = ["Python", "Hangman", "Programming", "OOP", "Student"]
    
    while True:
        game = Hangman(words)
        game.play()

        again = input("\nPlay again? (y/n): ").lower()
        if again not in ("y", "yes"):
            print("👋 Thanks for playing!")
            break
