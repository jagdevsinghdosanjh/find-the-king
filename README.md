# 🎮 Find the King – Streamlit Betting Game

An interactive card guessing game built with Streamlit. Players deposit money, guess the hidden King among shuffled cards, and bet to grow their wallet.

## 🧠 Game Rules
- Deposit any amount to start.
- Wallet is initialized to 2× deposit.
- Each round:
  - Cards (King, Queen, Jack) are shuffled.
  - Guess the King's position (1, 2, or 3).
  - Bet an amount ≤ wallet.
  - Correct guess → win 2× bet.
  - Wrong guess → lose bet.
- Game continues until wallet is zero or player quits.

## 🚀 How to Run
```bash
pip install -r requirements.txt
streamlit run main.py
