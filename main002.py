import streamlit as st
from utils import shuffle_cards, evaluate_guess, get_card_image, log_game_round

st.set_page_config(page_title="Find the King", layout="centered")

# Session state
if 'wallet' not in st.session_state:
    st.session_state.wallet = 0
if 'game_started' not in st.session_state:
    st.session_state.game_started = False

# Deposit
if not st.session_state.game_started:
    deposit = st.number_input("💵 Enter deposit amount", min_value=1)
    if st.button("Start Game"):
        st.session_state.wallet = deposit * 2
        st.session_state.game_started = True
        st.success(f"Game started! Wallet: ${st.session_state.wallet}")

# Game loop
if st.session_state.game_started and st.session_state.wallet > 0:
    st.write(f"💰 Wallet: ${st.session_state.wallet}")
    
    # Inputs
    bet_input = st.number_input("Place your bet", min_value=1, max_value=st.session_state.wallet)
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

        # Log the round
        log_game_round(bet, guess, king_pos, result, profit_loss, st.session_state.wallet)

    # Quit logic
    if st.button("Quit Game"):
        st.write(f"🏁 You walk away with ${st.session_state.wallet}")
        st.session_state.game_started = False
        st.session_state.wallet = 0
