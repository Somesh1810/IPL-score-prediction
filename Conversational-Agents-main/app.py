import streamlit as st
from game_state import GameState
from agent import play_round, explain_rules

st.set_page_config(page_title="RPS Plus Referee", layout="centered")

st.title("🎮 Rock–Paper–Scissors–Plus")
st.caption("AI Referee Bot (Best of 3)")

# Initialize game state
if "state" not in st.session_state:
    st.session_state.state = GameState()
    st.session_state.messages = []

# Show rules once
with st.expander("📜 Game Rules"):
    st.markdown("""
- Best of 3 rounds  
- Moves: **rock, paper, scissors, bomb**  
- **Bomb can be used once per player**  
- Bomb beats all moves  
- Invalid input wastes the round  
""")

state = st.session_state.state

# Game Over
if state.round == 3:
    st.markdown("## 🏁 GAME OVER")

    st.markdown(
        f"### Final Score → You: {state.user_score} | Bot: {state.bot_score}"
    )

    if state.user_score > state.bot_score:
        st.markdown("## 🎉 Result: USER WINS")
    elif state.bot_score > state.user_score:
        st.markdown("## 🤖 Result: BOT WINS")
    else:
        st.markdown("## 🤝 Result: DRAW")

    if st.button("🔄 Restart Game"):
        st.session_state.state = GameState()
        st.session_state.messages = []
        st.experimental_rerun()


else:
    st.subheader(f"Round {state.round + 1}")

    user_move = st.selectbox(
        "Choose your move",
        ["rock", "paper", "scissors", "bomb"]
    )

    if st.button("Play Move"):
        st.session_state.state, response = play_round(state, user_move)
        st.session_state.messages.append(response)

# Display round history
if st.session_state.messages:
    st.divider()
    st.subheader("🧾 Game Log")
    for msg in st.session_state.messages:
        st.text(msg)
