import random

class Hangman:
    def __init__(self, word_list, max_attempts=6):
        self.word = random.choice(word_list).lower()   # Pick a random word
        self.guessed_letters = []              # Store letters guessed
        self.wrong_guesses = []                # Store wrong guesses
        self.max_attempts = max_attempts       # Limit of wrong guesses
        self.attempts_left = max_attempts

    def display_word(self):
        # Show the word with underscores for unguessed letters
        display = ""
        for letter in self.word:
            if letter in self.guessed_letters:
                display += letter + " "
            else:
                display += "_ "
        return display.strip()

    def guess(self, letter):
        # Handle a guess
        if not (len(letter) == 1 and letter.isalpha()): #Validate input
            print("❌ Invalid input! Enter a single letter.\n")
            return
        
        if letter in self.guessed_letters or letter in self.wrong_guesses: #Check if letter was already guessed
            print("⚠️ Already guessed!\n")
            return
        
        elif letter in self.word: #Check if letter is in the word
            print("✅ Correct guess!\n")
            self.guessed_letters.append(letter)
        else: #If letter not in the word, decrease attempts left
            print("❌ Wrong guess!\n")
            self.wrong_guesses.append(letter)
            self.attempts_left -= 1

    def is_won(self):
        # Check if all letters are guessed
        return all(letter in self.guessed_letters for letter in self.word)

    def is_lost(self):
        # Check if attempts are finished
        return self.attempts_left <= 0
    
    def display_hangman(self):
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
        
        # Wrong attempts = max_attempts - attempts_left
        wrong_attempts = self.max_attempts - self.attempts_left
        return stages[wrong_attempts]
    
    def print_status(self):
        print(self.display_hangman())
        print("Word:", self.display_word())
        print("Correct guesses:", ', '.join(self.guessed_letters) if self.guessed_letters else "None")
        print("Wrong guesses:", ', '.join(self.wrong_guesses) if self.wrong_guesses else "None")
        print("Attempts left:", self.attempts_left, "\n")

    
    def play(self):
        print("🎉 Welcome to Hangman! 🎉")
        print("\nYour word contains", len(self.word), "letters.\n")
        
        while not self.is_won() and not self.is_lost():
            self.print_status()
            guess = input("Enter a letter: ").lower()
            self.guess(guess)
            
        if self.is_won():
            print("\n🎉 You won! The word was:", self.word)
        else:
            print(self.display_hangman())
            print("\n💀 You lost! The word was:", self.word)
                


# ---------------- MAIN GAME LOOP ----------------
if __name__ == "__main__":
    words = ["Python", "Hangman", "Programming", "OOP", "Student"]
    while True:
        game = Hangman(words, max_attempts=8)
        game.play()
        again = input("\nPlay again? (y/n): ").lower()
        if again not in ("y", "yes"):
            print("👋 Thanks for playing!")
            break
