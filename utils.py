import random
import csv
import os

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

def log_game_round(bet, guess, king_pos, result, profit_loss, wallet, initial_deposit, total_won):
    folder_path = "assets/cash_won_lost"
    log_path = os.path.join(folder_path, "game_log.csv")

    os.makedirs(folder_path, exist_ok=True)
    file_exists = os.path.isfile(log_path)

    with open(log_path, mode='a', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        if not file_exists:
            writer.writerow([
                "Initial Deposit", "Bet", "Guess", "King Position",
                "Result", "Profit/Loss", "Wallet Balance", "Total Won"
            ])
        writer.writerow([
            initial_deposit, bet, guess, king_pos,
            result, profit_loss, wallet, total_won
        ])
