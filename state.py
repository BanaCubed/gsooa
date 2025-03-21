import json
from typing import TypedDict, TYPE_CHECKING

from jinja2 import Undefined

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
"""
A dictionary representing values shared across files that are not saved across sessions
"""
# endregion


# region Stable
class StableStateType(TypedDict):
    totalScore: int
    """The total score accumulated across all completed games"""
    bestScore: int
    """The highest amount of score reached within a singular game"""


# TODO change unstableState to use something similar
class _StableStateClass:
    """
    A private class representing the type of stableState
    """
    value: StableStateType
    """The actual state"""

    def __init__(self) -> None:
        defaultState: StableStateType = {
            "totalScore": 0,
            "bestScore": 0,
        }
        try:
            open("userdata", "x")
            self.value = defaultState
        except FileExistsError:
            try:
                with open("userdata", "r") as file:
                    self.value = json.loads(file.read().replace("'", '"'))
                for attr in defaultState:
                    if self.value[attr] != Undefined:
                        self.value[attr] = defaultState[attr]
            except json.decoder.JSONDecodeError:
                self.value = defaultState

    def setValue(self, name, value):
        self.value.update({name: value})
        with open("userdata", "w") as file:
            file.write(str(self.value))


stableState = _StableStateClass()
"""
A variables containing two properties.

1. `value`: The actual state.
2. `setValue(name, value)`: A function to update `value`, and saves it to ./userdata
"""
# endregion
