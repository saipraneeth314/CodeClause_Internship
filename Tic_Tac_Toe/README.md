# Tic-Tac-Toe AI Game (Python + Tkinter + Minimax)

A simple yet smart Tic-Tac-Toe game built using **Python** and **Tkinter GUI**, where you play against an AI powered by the **Minimax algorithm**.

---

## Screenshot

> *(Add a screenshot of the game window here after running the app)*  
> ![Game Screenshot](screenshot.png)

---

## Features

- Intuitive GUI using **Tkinter**
- Smart AI using **Minimax algorithm**
- Message pop-ups for win, lose, and draw

---

## How to Run

### 1. **Clone the Repository**
```bash
git clone https://github.com/your-username/Tic_Tac_Toe_AI.py.git
cd Tic_Tac_Toe
```

### 2. **Run the App**
```bash
python Tic_Tac_Toe_AI.py
```

> Make sure you have Python 3 installed.

---

## Game Rules

- Player is `"X"` and goes first.
- AI is `"O"` and plays automatically after your move.
- Win by placing 3 of your symbols in a row (horizontal, vertical, or diagonal).

---

## How Minimax Works

The AI simulates every possible move for both itself and the player:
- **+1** if AI can win  
- **-1** if AI lets player win  
- **0** for draw  

It then selects the move that **maximizes its chances of winning**, assuming you also play optimally.

---

## Tech Stack

| Component | Technology |
|----------|-------------|
| Language | Python |
| GUI      | Tkinter |
| AI       | Minimax Algorithm |

---

## File Structure

```
tic-tac-toe-ai/
├── Tic_Tac_Toe_AI.py   # Main Python file with GUI + AI logic
├── README.md           # Project documentation
└── screenshot.png      # Game preview image
```

---

## Author

**Kasam Sai Praneeth**  
GitHub: [@saipraneeth314](https://github.com/saipraneeth314)