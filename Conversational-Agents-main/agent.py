"""
AGENT ORCHESTRATION LAYER

The agent:
- Interprets user intent
- Calls tools for validation and state mutation
- Generates user-facing responses

No game logic lives in prompts or responses.
"""


from tools import validate_move, resolve_round, update_game_state
from game_state import GameState

def explain_rules():
    print("""
Rules:
• Best of 3 rounds
• Moves: rock, paper, scissors, bomb (once)
• Bomb beats everything
• Invalid input wastes the round
""")

def play_round(state: GameState, user_input: str):
    result = validate_move(user_input, state.user_bomb_used)

    if not result["valid"]:
        state.round += 1
        return state, f"Invalid input ({result['reason']}). Round wasted."

    bot_move, winner = resolve_round(user_input, state)
    state = update_game_state(state, winner, user_input, bot_move)

    response = (
        f"Round {state.round}\n"
        f"You played: {user_input}\n"
        f"Bot played: {bot_move}\n"
        f"Winner: {winner}"
    )

    return state, response
