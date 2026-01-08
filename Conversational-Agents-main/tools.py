"""
ADK TOOL DEFINITIONS

These functions are designed to be registered as Google ADK tools.
They perform deterministic logic and mutate game state.

Tools:
- validate_move
- resolve_round
- update_game_state
"""


import random
from game_state import GameState

VALID_MOVES = ["rock", "paper", "scissors", "bomb"]

def validate_move(move: str, bomb_used: bool) -> dict:
    if move not in ["rock", "paper", "scissors", "bomb"]:
        return {
            "valid": False,
            "reason": "Invalid move"
        }

    if move == "bomb" and bomb_used:
        return {
            "valid": False,
            "reason": "Bomb already used"
        }

    return {
        "valid": True
    }


def resolve_round(user_move: str, state: GameState):
    bot_choices = ["rock", "paper", "scissors"]
    if not state.bot_bomb_used:
        bot_choices.append("bomb")

    bot_move = random.choice(bot_choices)

    if user_move == "bomb":
        state.user_bomb_used = True
    if bot_move == "bomb":
        state.bot_bomb_used = True

    if user_move == bot_move:
        winner = "draw"
    elif user_move == "bomb":
        winner = "user"
    elif bot_move == "bomb":
        winner = "bot"
    elif (
        (user_move == "rock" and bot_move == "scissors") or
        (user_move == "paper" and bot_move == "rock") or
        (user_move == "scissors" and bot_move == "paper")
    ):
        winner = "user"
    else:
        winner = "bot"

    return bot_move, winner


def update_game_state(state: GameState, winner: str, user_move, bot_move):
    state.round += 1

    if winner == "user":
        state.user_score += 1
    elif winner == "bot":
        state.bot_score += 1

    state.history.append({
        "round": state.round,
        "user_move": user_move,
        "bot_move": bot_move,
        "winner": winner
    })

    return state
