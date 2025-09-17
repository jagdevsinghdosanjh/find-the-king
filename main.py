import streamlit as st
import pandas as pd
import os
from utils import shuffle_cards, evaluate_guess, get_card_image, log_game_round, is_csv_valid

st.set_page_config(page_title="Find the King", layout="centered")
st.write("Welcome to Online Game - Find the King")

# Session state
if 'wallet' not in st.session_state:
    st.session_state.wallet = 0
if 'game_started' not in st.session_state:
    st.session_state.game_started = False
if 'initial_deposit' not in st.session_state:
    st.session_state.initial_deposit = 0
if 'total_won' not in st.session_state:
    st.session_state.total_won = 0

log_path = "assets/cash_won_lost/game_log.csv"

# Deposit
if not st.session_state.game_started:
    deposit = st.number_input("💵 Enter deposit amount", min_value=1)
    if st.button("Start Game"):
        st.session_state.wallet = deposit * 2
        st.session_state.initial_deposit = deposit
        st.session_state.total_won = 0
        st.session_state.game_started = True
        st.success(f"Game started! Wallet: ${st.session_state.wallet}")

# Game loop
if st.session_state.game_started and st.session_state.wallet > 0:
    st.write(f"💰 Wallet: ${st.session_state.wallet}")

    if st.session_state.wallet >= 1:
        bet_input = st.number_input(
            "Place your bet",
            min_value=1,
            max_value=st.session_state.wallet
        )
        guess_input = st.selectbox("Guess the King's position", [1, 2, 3])

        # Reveal logic
        if st.button("Reveal"):
            bet = bet_input
            guess = guess_input

            cards = shuffle_cards()
            st.session_state.wallet, result, king_pos = evaluate_guess(cards, guess, bet, st.session_state.wallet)
            st.write(result)
            st.write(f"🃏 King was at position {king_pos}")

            # Show card images
            cols = st.columns(3)
            for i, card in enumerate(cards):
                with cols[i]:
                    st.image(get_card_image(card), caption=f"Position {i+1}", width=150)

            # Calculate profit/loss
            profit_loss = bet * 2 if "won" in result else -bet

            # Update total won
            if profit_loss > 0:
                st.session_state.total_won += profit_loss

            # Log the round
            log_game_round(
                bet, guess, king_pos, result, profit_loss,
                st.session_state.wallet,
                st.session_state.initial_deposit,
                st.session_state.total_won
            )
    else:
        st.warning("💸 Your wallet is empty or too low to place a bet. Please restart the game.")

    # Quit logic
    if st.button("Quit Game"):
        st.write(f"🏁 You walk away with ${st.session_state.wallet}")
        st.session_state.game_started = False
        st.session_state.wallet = 0

# 📊 View Game History
if os.path.exists(log_path):
    if is_csv_valid(log_path):
        with st.expander("📊 View Game History"):
            df = pd.read_csv(log_path)
            st.dataframe(df, use_container_width=True)

            st.write(f"🔢 Total Rounds Played: {len(df)}")
            st.write(f"💰 Net Profit/Loss: ${df['Profit/Loss'].sum()}")

            st.line_chart(df["Wallet Balance"], use_container_width=True)

            if st.button("🧹 Reset Game Log", key="reset_log_valid"):
                os.remove(log_path)
                st.success("Game log has been reset.")
    else:
        st.error("⚠️ Game log is malformed. Some rows have inconsistent columns.")
        if st.button("🧹 Force Reset Game Log", key="reset_log_invalid"):
            os.remove(log_path)
            st.success("Malformed log has been cleared.")

# 🔄 Restart Game
if st.button("🔄 Restart Game"):
    st.session_state.wallet = 0
    st.session_state.initial_deposit = 0
    st.session_state.total_won = 0
    st.session_state.game_started = False

    if os.path.exists(log_path):
        os.remove(log_path)

    st.success("Game has been reset. You can start fresh with a new deposit.")
