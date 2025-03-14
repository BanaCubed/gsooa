from typing import TypedDict


# region State Setup
class UnstableState(TypedDict):
    running: bool
    seed: int
    prngRuns: int


unstableState: UnstableState = {
    "running": False,  # Whether the game is currently running
    "seed": 0,  # Current seed used for PRNG calculations
    "prngRuns": 0,  # Number of times the PRNG has been called
}
"""
`unstableState` tracks the mutable game state that changes frequently during a session.

Fields:
- `running`: Boolean indicating if game is active
- `seed`: Integer seed value used by PRNG for randomization
- `prngRuns`: Counter tracking number of PRNG function calls
"""


class StableState(TypedDict):
    totalScore: int


stableState: StableState = {
    "totalScore": 0,  # Total accumulated score across all games
}
"""
`stableState` tracks persistent game state that persists between sessions.

Fields:
- `totalScore`: Integer representing cumulative score from all finished sessions
"""
# endregion
