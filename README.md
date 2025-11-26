# Star Wars Quiz

An interactive command-line quiz game to test your Star Wars knowledge! Challenge yourself with questions ranging from easy trivia to absolute nerd-level deep cuts.

## Features

- **Multiple Difficulty Levels**: Choose from Easy, Medium, Absolute Nerd, or take on all questions
- **Randomized Questions**: Questions are shuffled each time for a fresh experience
- **Interactive Interface**: Clean, formatted output with visual separators
- **Quit Anytime**: Press 'q' during any question to exit early
- **Score Tracking**: See your final score and how many questions you completed
- **Command-Line Arguments**: Quick start by passing difficulty as an argument
- **Color-Coded Feedback**: Visual indicators for correct/incorrect answers (may not work properly on Windows, but what does?)
- **Cross-Platform Support**: Works on Linux, Mac, and even Windows (though we can't promise the same level of enjoyment)

## Installation

No special installation required! Just ensure you have Python 3 installed.

### Linux/Mac
```bash
# Clone or download this repository
cd starwarsquiz

# Run the quiz
python3 star_wars_quiz.py
```

### Windows *(sigh)*
```cmd
# Clone or download this repository
cd starwarsquiz

# Run the quiz (if this doesn't work, try updating your PATH, reinstalling Python, 
# sacrificing a chicken to the registry gods, or just use a real operating system)
python star_wars_quiz.py
```

> **Note:** If you're experiencing issues on Windows, have you considered switching to Linux? It's free, stable, and doesn't randomly restart for updates mid-quiz.

## Usage

### Interactive Mode

**Linux/Mac:**
```bash
python3 star_wars_quiz.py
```

**Windows:**
```cmd
python star_wars_quiz.py
```

Then select your difficulty:
1. Easy
2. Medium
3. Absolute Nerd
4. All Questions

### Quick Start with Arguments

**Linux/Mac:**
```bash
python3 star_wars_quiz.py 1    # Easy mode
python3 star_wars_quiz.py 2    # Medium mode
python3 star_wars_quiz.py 3    # Absolute Nerd mode
python3 star_wars_quiz.py 4    # All questions
```

**Windows:**
```cmd
python star_wars_quiz.py 1    # Easy mode
python star_wars_quiz.py 2    # Medium mode
python star_wars_quiz.py 3    # Absolute Nerd mode
python star_wars_quiz.py 4    # All questions
```

You can also use the difficulty name:

**Linux/Mac:**
```bash
python3 star_wars_quiz.py easy
python3 star_wars_quiz.py medium
python3 star_wars_quiz.py "absolute nerd"
```

**Windows:**
```cmd
python star_wars_quiz.py easy
python star_wars_quiz.py medium
python star_wars_quiz.py "absolute nerd"
```

## Question Format

Questions are stored in `questions.json` with the following structure:
- `question`: The question text
- `choices` (or `options`): Array of answer options
- `correct_index`: Index of the correct answer (0-based)
- `category`: Difficulty level (easy, medium, absolute nerd)

## Project Structure

```
starwarsquiz/
├── star_wars_quiz.py           # Main quiz application
├── questions.json              # Quiz questions database
└── README.md                   # This file
```

## Troubleshooting

### The colors don't work!
- **Linux/Mac:** This shouldn't happen. Check your terminal.
- **Windows:** Of course they don't. Try Windows Terminal instead of CMD, or better yet, install WSL.

### Python command not found!
- **Linux/Mac:** Install Python 3 using your package manager.
- **Windows:** Welcome to PATH variable hell. Google "add Python to PATH Windows" and prepare for a journey. Or save yourself the headache and dual-boot Linux.

### The quiz works perfectly!
- **Linux/Mac:** As expected.
- **Windows:** Congratulations! You've achieved the impossible. Screenshot it before Windows Update breaks it.

## Contributing

To add new questions, edit `questions.json` following the existing format. Ensure each question has:
- Clear question text
- Answer choices (use either `choices` or `options` as the key)
- The correct answer index (0-based)
- An appropriate category (easy, medium, or absolute nerd)

