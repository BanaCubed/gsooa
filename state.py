from typing import TypedDict, TYPE_CHECKING

if TYPE_CHECKING:
    from questions import Question


# region Unstable
class UnstableStateType(TypedDict):
    running: bool
    """Whether or not the game is currently active"""
    seed: int
    """The current games seed used for PRNG calculations"""
    prngRuns: int
    """The number of times PRNG has been used in the current game"""
    level: int
    """The current difficulty level the running game has reached"""
    score: int
    """The current score of the running game"""
    question: 'Question | None'
    """The current question being answered"""


unstableState: UnstableStateType = {
    "running": False,
    "seed": 0,
    "prngRuns": 0,
    "level": 0,
    "score": 0,
    "question": None,
}
# endregion


# region Stable
class StableStateType(TypedDict):
    totalScore: int
    """The total score accumulated across all completed games"""


stableState: StableStateType = {
    "totalScore": 0,
}
# endregion
