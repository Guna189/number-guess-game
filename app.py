import streamlit as st
import random

st.title("🎯 Number Guessing Game")

# Initialize session state
if "number" not in st.session_state:
    st.session_state.number = None
if "started" not in st.session_state:
    st.session_state.started = False
if "turns" not in st.session_state:
    st.session_state.turns = 0

# Input fields
lower = st.number_input("Enter lower range", value=1)
upper = st.number_input("Enter upper range", value=100)

# Start button
if st.button("Start Game"):
    if lower >= upper:
        st.error("Lower range must be less than upper range!")
    else:
        st.session_state.number = random.randint(int(lower), int(upper))
        st.session_state.started = True
        st.session_state.turns = 0  # reset turns
        st.success("Game started! Start guessing...")

# Guess section
if st.session_state.started:
    guess = st.number_input("Enter your guess", step=1)

    if st.button("Submit Guess"):
        st.session_state.turns += 1  # increment turns

        if guess < st.session_state.number:
            st.warning("🔼 Try a higher number!")
        elif guess > st.session_state.number:
            st.warning("🔽 Try a lower number!")
        else:
            st.success(f"🎉 Correct! You guessed the number in {st.session_state.turns} turns!")
            st.session_state.started = False

    st.info(f"Number of turns: {st.session_state.turns}")
