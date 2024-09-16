# Tic-Tac-Toe AI with Minimax Algorithm

Welcome to the **Tic-Tac-Toe AI** project! This Python-based application lets you play a game of Tic-Tac-Toe against an unbeatable AI powered by the **Minimax Algorithm**. The AI analyzes all possible moves to find the optimal strategy, ensuring a fair yet challenging game experience.

## Features

- **Single-player mode**: Play against an AI that always makes the optimal move.
- **Unbeatable AI**: Uses the Minimax algorithm, making it impossible to beat the AI when it plays first or second.
- **Simple and intuitive interface**: A text-based interface with a 3x3 grid, where players input their moves by selecting grid positions.
- **Auto-reset**: The game resets the board after each round.

## Table of Contents

1. [Installation](#installation)
2. [How to Play](#how-to-play)
3. [How it Works](#how-it-works)
4. [Future Enhancements](#future-enhancements)
5. [Contributing](#contributing)
6. [License](#license)

---

## Installation

To get started, follow the steps below to set up and run the Tic-Tac-Toe AI:

### Prerequisites

- Python 3.8 or higher
- A terminal (running on Ubuntu via WSL2 for Windows, or any Linux/Mac terminal)
- Optional: Jupyter Notebook for interactive testing

### Setup Instructions

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/tictactoe-ai.git
   cd tictactoe-ai
   ```

2. Set up a Python virtual environment:
   ```bash
   python3 -m venv .venv
   source .venv/bin/activate  # On Linux/macOS
   ```

3. Install dependencies:
   ```bash
   pip install jupyter
   ```

4. Run the program:
   ```bash
   python3 tictactoe.py
   ```

### Optional: Jupyter Notebook Setup

To experiment with the game logic in an interactive notebook:
```bash
pip install notebook
jupyter notebook
```

## How to Play

1. **Start the game** by running the script.
2. You’ll be greeted with an empty 3x3 board, represented as a grid:
   ```
   |   |   |   |
   |   |   |   |
   |   |   |   |
   ```
3. **Input your move** by selecting a grid position (1-9) based on this layout:
   ```
   1 | 2 | 3
   4 | 5 | 6
   7 | 8 | 9
   ```
4. **Watch the AI make its move** after you make yours.
5. The game will continue until there's a win, loss, or draw, and the board will reset for a new game.

## How it Works

This Tic-Tac-Toe AI uses the **Minimax Algorithm**, a classic algorithm in game theory, to evaluate all possible moves and select the best one. Here's a quick overview of how it works:

- **Minimax Algorithm**: The AI searches the game tree recursively, evaluating potential future moves, and assigning scores based on win/loss outcomes.
- **Optimal Strategy**: The AI will always make the move that maximizes its chance of winning or, at worst, results in a draw.

#### Example Move Strategy

- If there's a chance to win, the AI will take it.
- If the player is about to win, the AI will block the move.
- If neither of these conditions apply, the AI selects the best available move based on Minimax scoring.

## Future Enhancements

Here are some features we plan to add in future releases:

- **GUI version**: Implement a graphical interface using `Tkinter` or `Pygame` for a more user-friendly experience.
- **Multiplayer mode**: Add support for human vs human gameplay on the same machine.
- **Difficulty levels**: Implement adjustable difficulty by restricting the depth of the Minimax search.

## Contributing

We welcome contributions from the community! Here’s how you can help:

1. Fork the repository.
2. Create a feature branch (`git checkout -b feature/new-feature`).
3. Commit your changes (`git commit -m "Add new feature"`).
4. Push the branch (`git push origin feature/new-feature`).
5. Open a pull request, and we’ll review your changes.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more information.
