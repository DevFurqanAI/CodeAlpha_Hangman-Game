<p align="center">
  <img src="https://img.shields.io/badge/Python-3.8%2B-blue?style=for-the-badge">
  <img src="https://img.shields.io/badge/Status-Completed-brightgreen?style=for-the-badge">
  <img src="https://img.shields.io/badge/Category-Console%20Game-orange?style=for-the-badge">
</p>

A clean, object-oriented Hangman game built in Python using ASCII art, input validation, and a polished console interface.  
Perfect for beginners learning OOP or anyone who wants a fun terminal game!

---

## ✨ Key Features
- 🎲 Random word selection from a custom list  
- 🧩 Progress display with underscores for hidden letters  
- ❌ Wrong-guess tracking with remaining attempts  
- 🧠 Input validation (single alphabetic letters only)  
- 🎨 ASCII Hangman stages that update on each wrong attempt  
- 🔁 Play again option at the end of each match  
- 🧱 Object-Oriented structure using a clean Hangman class  

---

## 📁 Project Files
hangman.py # Main game logic and program entry point
README.md # Project documentation

---

## 🚀 Getting Started

### 1. Install Python
Ensure Python 3.x is installed.  
Check using:

```bash
python --version
```

### 2. Run the Game
```bash
python hangman.py
```

### 3. Play the Game
Guess letters, avoid mistakes, and try to reveal the entire word!

---

## 🕹️ Gameplay Overview
- You get 6 wrong attempts (default)
- Correct letters appear in their positions
- Each incorrect guess builds the hangman
- Game ends when:
  - 🎉 You guess all letters, or
  - 💀 You run out of attempts

---

## 🧱 Code Structure (OOP)
| Method              | Purpose                             |
| ------------------- | ----------------------------------- |
| `display_word()`    | Shows guessed letters + underscores |
| `guess(letter)`     | Processes a guess                   |
| `is_won()`          | Checks win condition                |
| `is_lost()`         | Checks lose condition               |
| `display_hangman()` | ASCII art stages                    |
| `print_status()`    | Prints current game info            |
| `play()`            | Runs the game loop                  |

---

## 🎨 Hangman Stages (Preview)
```bash
Wrong guess 0:
   ------
   |    |
   |
   |
   |
   |

Wrong guess 6:
   ------
   |    |
   |    O
   |   /|\
   |   / \
   |
```

---

## 🧰 Customization
🔹Add your own words
```bash
words = ["Laptop", "Developer", "Algorithm", "Database", "Network"]
```

🔹Change maximum allowed attempts
```bash
game = Hangman(words, max_attempts=8)
```

🧪 Sample Word List (Default)
```bash
words = ["Python", "Hangman", "Programming", "OOP", "Student"]
```

---

## 🤝 Contributing
If you'd like to enhance the game (GUI version, difficulty levels, animations), feel free to open a pull request or fork the project.

---

## 📜 License
This project is free to use, modify, and share.
