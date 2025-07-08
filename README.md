# WAR-Card-game
A card game using Object oriented programming (OOPs) in Python .

# ♠️ WAR: Python Card Game

This project is a Python implementation of the classic card game "War" between two players — in this case, GOJO and GETO.

## 📜 Game Rules

- A standard 52-card deck is divided equally between two players.
- Each round, both players draw the top card of their deck.
- The player with the higher card value wins the round and collects both cards.
- If the cards are equal, a "WAR" occurs:
  - Each player places 5 additional cards.
  - The 6th card (last one added) is compared.
  - The player with the higher 6th card wins all cards on the table.
  - If a player doesn’t have enough cards (i.e., < 5) to continue WAR, they lose.

## 🧠 Program Structure

### `Card` Class
- Represents a single playing card.
- Stores suit, rank, and its numerical value.

### `Deck` Class
- Creates and holds a full shuffled deck of 52 cards.
- Deals cards using `pick_one_card()`.

### `Player` Class
- Holds each player's cards in a list.
- Supports adding and removing cards.

### Game Loop
- Continuously plays rounds until one player runs out of cards.
- Handles comparison of cards and WAR scenarios.

## 💡 Key Features

- Clean OOP structure (Object-Oriented Programming).
- Handles recursive "WAR" logic with safeguards for edge cases.
- Includes print statements to trace the game round-by-round.

## 📌 Requirements

- Python 3.x
- No external libraries required (only built-in `random`)

## 🚀 How to Run

```bash
python "MILESTONE 2.py"
```

> Make sure the filename matches your script.

## 🔚 Game End

- The game ends when a player runs out of cards.
- In a WAR situation, if a player cannot provide 5 cards, they immediately lose.

---

📂 **Contributions** are welcome! Feel free to fork, suggest optimizations, or add enhancements.

---

🃏 Happy Coding and may the best deck win!
