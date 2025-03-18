from typing import TypedDict


# region State Setup
class UnstableStateType(TypedDict):
    running: bool
    """
    Whether or not the game is currently active
    """
    seed: int
    """
    The current games seed used for PRNG calculations
    """
    prngRuns: int
    """
    The number of times PRNG has been used in the current game
    """
    level: int
    """
    The current difficulty level the running game has reached
    """


unstableState: UnstableStateType = {
    "running": False,
    "seed": 0,
    "prngRuns": 0,
    "level": 0,
}
"""
`unstableState` tracks the mutable game state that changes frequently during a session.

Fields:
- `running`: Boolean indicating if game is active
- `seed`: Integer seed value used by PRNG for randomization
- `prngRuns`: Counter tracking number of PRNG function calls
"""


class StableStateType(TypedDict):
    totalScore: int


stableState: StableStateType = {
    "totalScore": 0,  # Total accumulated score across all games
}
"""
`stableState` tracks persistent game state that persists between sessions.

Fields:
- `totalScore`: Integer representing cumulative score from all finished sessions
"""
# endregion
