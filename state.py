import json
from typing import Any, TypedDict, TYPE_CHECKING

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
    num: int
    """The index of the current question being answered in the current game"""
    hp: int
    """The remaining questions answered incorrectly until the current game is lost"""
    xp: int
    """Cumulative experience points earned in the current game"""


unstableState: UnstableStateType = {
    "running": False,
    "seed": 0,
    "prngRuns": 0,
    "level": 0,
    "score": 0,
    "question": None,
    "num": 0,
    "hp": 0,
    "xp": 0,
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
    bestLevel: int
    """The highest level reached within a sungular game"""


# TODO change unstableState to use something similar
class _StableStateClass:
    """
    A private class representing the type of stableState
    """
    value: StableStateType
    """The actual state"""

    def __init__(self) -> None:
        self.value = {
            "totalScore": 0,
            "bestScore": 0,
            "bestLevel": 0,
        }
        try:
            open("userdata", "x")
        except FileExistsError:
            try:
                with open("userdata", "r") as file:
                    loadedState: StableStateType = json.loads(
                        file.read().replace("'", '"')
                    )
                for attr in self.value:
                    try:
                        self.value[attr] = loadedState[attr]
                    except KeyError:
                        pass
            except json.decoder.JSONDecodeError:
                pass

    def setValue(self, name: str, value: Any):
        self.value.update({name: value})  # type: ignore
        with open("userdata", "w") as file:
            file.write(str(self.value))


stableState = _StableStateClass()
"""
A variables containing two properties.

1. `value`: The actual state.
2. `setValue(name, value)`: A function to update `value`, and saves it to ./userdata
"""
# endregion


if __name__ == "__main__":
    print(stableState.value)
