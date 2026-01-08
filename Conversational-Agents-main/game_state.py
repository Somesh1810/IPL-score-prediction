from dataclasses import dataclass, field

@dataclass
class GameState:
    round: int = 0
    user_score: int = 0
    bot_score: int = 0
    user_bomb_used: bool = False
    bot_bomb_used: bool = False
    history: list = field(default_factory=list)
