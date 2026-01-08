from agent import explain_rules, play_round
from game_state import GameState

def run_game():
    state = GameState()
    explain_rules()

    while state.round < 3:
        user_input = input(f"\nRound {state.round + 1} - Enter your move: ").lower().strip()
        state, response = play_round(state, user_input)
        print(response)

    print("\n=== GAME OVER ===")
    print(f"Final Score → You: {state.user_score} | Bot: {state.bot_score}")

    if state.user_score > state.bot_score:
        print("Result: USER WINS 🎉")
    elif state.bot_score > state.user_score:
        print("Result: BOT WINS 🤖")
    else:
        print("Result: DRAW 🤝")

if __name__ == "__main__":
    run_game()
