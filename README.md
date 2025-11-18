# 🎮 Sudoku Master

[![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)](https://www.python.org/)
[![Tkinter](https://img.shields.io/badge/Tkinter-Built--in-orange.svg)](https://docs.python.org/3/library/tkinter.html)
[![License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)

**Sharpen your mind with Sudoku Master – a sleek, professional Sudoku game built with Python and Tkinter!**  
Challenge yourself with variable grid sizes across three difficulty levels: Easy (5x5), Medium (7x7), and Hard (10x10). Enjoy a modern dark-themed UI with intuitive controls and real-time validation.

![Sudoku Master Screenshot](https://via.placeholder.com/700x850/121212/00BFA5?text=Sudoku+Master+Gameplay)  
*Example gameplay interface showcasing the dark theme and grid layout.*

## ✨ Features

- **🎯 Multiple Difficulty Levels**: Choose from Easy (5x5), Medium (7x7), or Hard (10x10) puzzles to match your skill.
- **🔄 Dynamic Puzzle Generation**: Automatically generates solvable puzzles by filling the board and removing cells based on difficulty.
- **✅ Real-Time Validation**: Input validation ensures only valid numbers (1 to grid size) are accepted, with visual feedback.
- **🎨 Modern UI Design**: Dark-themed interface with teal accents, clean fonts (Segoe UI), and hover effects for buttons.
- **🧩 Solution Checking**: Verify your solution with a single click – get instant feedback on correctness.
- **🔄 New Game Anytime**: Start a fresh puzzle at any time without restarting the app.
- **📱 Responsive Layout**: Fixed window size (700x850) optimized for desktop play.

## 🚀 Installation

### Prerequisites
- **Python 3.8 or higher** installed on your system. Download from [python.org](https://www.python.org/downloads/).
- Tkinter is included with Python by default (no separate installation needed).

### Steps
1. **Clone or Download the Repository**:
   ```bash
   git clone https://github.com/yourusername/sudoku-master.git
   cd sudoku-master
   ```

2. **Run the Game**:
   ```bash
   python main.py
   ```
   - The Sudoku Master window will launch immediately.

## 🎮 Usage

1. **Launch the App**: Run `python main.py` to open the game window.
2. **Select Difficulty**: Use the radio buttons to choose Easy, Medium, or Hard.
3. **Start Playing**:
   - The grid will populate with a new puzzle.
   - Click on empty cells and type numbers (1 to grid size).
   - Pre-filled cells are disabled and highlighted.
4. **Validate Input**: Invalid entries are automatically cleared; valid ones turn green.
5. **Check Solution**: Click "✔️ Check Solution" to verify if the puzzle is solved correctly.
6. **New Game**: Click "🧩 New Game" to generate a fresh puzzle at the current difficulty.
7. **Exit**: Click "❌ Exit" to close the application.

### Controls
- **Keyboard**: Type numbers directly into cells.
- **Mouse**: Click buttons for actions.

## 📸 Screenshots

- **Main Interface**: Dark background with title, difficulty selector, grid, and buttons.
- **Gameplay**: Highlighted pre-filled cells, user input with color feedback.
- **Solution Check**: Pop-up messages for success or errors.

*(Add actual screenshots by replacing the placeholder image URL in the README.)*

## 🤝 Contributing

We welcome contributions! Here's how you can help:

1. Fork the repository.
2. Create a feature branch: `git checkout -b feature/your-feature`.
3. Make changes and test thoroughly.
4. Commit: `git commit -m 'Add your feature'`.
5. Push: `git push origin feature/your-feature`.
6. Open a Pull Request.

### Guidelines
- Follow PEP 8 for Python code.
- Test on multiple difficulty levels.
- Ensure UI remains responsive and accessible.

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- Built with Python and Tkinter for simplicity and cross-platform compatibility.
- Inspired by classic Sudoku puzzles – enjoy the challenge!

---

**Enjoy playing Sudoku Master? Star the repo ⭐ and share with friends!**  
For issues or suggestions, open an [issue](https://github.com/yourusername/sudoku-master/issues) on GitHub.
