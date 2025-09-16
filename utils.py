## 🧠 `utils.py`
import random

def shuffle_cards():
    cards = ["King", "Queen", "Jack"]
    random.shuffle(cards)
    return cards

def evaluate_guess(cards, guess, bet, wallet):
    king_position = cards.index("King") + 1
    if guess == king_position:
        wallet += bet * 2
        result = f"✅ Correct! You won ${bet * 2}"
    else:
        wallet -= bet
        result = f"❌ Wrong! You lost ${bet}"
    return wallet, result, king_position

def get_card_image(card_name):
    return f"assets/card_images/{card_name.lower()}.png"

