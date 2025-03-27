import math
import random

from questions import generateQuestion
from render import render
from state import unstableState, stableState


# region Play
def play(seed: int | None = None):
    """Initialize a run of the game"""
    render(
        "gsooA - starting"
    )
    # TODO add seed config, should have downside
    # TODO allow for choosing start level
    unstableState.update({
        "running": True,
        "seed": random.randint(0, 2**64) if seed is None else seed,
        "prngRuns": 0,
        "level": 1,
        "score": 0,
        "num": 0,
        "hp": 5,
        "xp": 0,
    })
    while unstableState["running"] is True:
        unstableState.update({
            "question": generateQuestion(),
            "num": unstableState["num"] + 1,
        })
        render(
            "gsooA - playing",
            "",
            f"| lv {unstableState["level"]}",
            f"| xp [{"#" * getXPInLevel(unstableState["xp"])}{
                " " * (min(unstableState["level"] + 3, 15) - getXPInLevel(unstableState["xp"]))}]",
            f"| hp [{"#" * unstableState["hp"]}{" " * (5 - unstableState["hp"])}]",
            "|",
            f"| question {unstableState["num"]}",
            f"| {unstableState["question"]}\n     |",
        )

        ans = 0
        while True:
            try:
                ans = float("".join(
                    input("     | > ").lower().split()
                ))
                break
            except ValueError:
                print("     | answer could not be interpereted. try again")

        if unstableState["question"].verifyAnswer(  # TODO remove need to check is not None
            str(ans)  # TODO remove need to stringify answer
        ) if unstableState["question"] is not None else False:
            unstableState.update({
                "score": unstableState["score"] + 1,  # TODO increase score per question with level
                "xp": unstableState["xp"] + 1,
            })
            unstableState.update({
                "level": getLevelAtXP(unstableState["xp"])
            })
        else:
            unstableState.update({
                "hp": unstableState["hp"] - 1
            })
            if unstableState["hp"] <= 0:
                lose()
                break

    render(
        "gsooA - results",
        "",
        f"| score - {unstableState["score"]}",
        f"| level - {unstableState["level"]}",
        "|",
        "| press enter to close\n     |",
    )
    input("     | > ")
# endregion


# region Lose
def lose():
    unstableState.update({"running": False})
    stableState.setValue("totalScore", stableState.value["totalScore"] + unstableState["score"])
    stableState.setValue("bestScore", max(stableState.value["bestScore"], unstableState["score"]))
    stableState.setValue("bestLevel", max(stableState.value["bestLevel"], unstableState["level"]))
# endregion


# region Leveling
def getLevelAtXP(xp: int) -> int:
    """Returns the level that a given amount of XP would place at"""
    if xp >= 95:
        return math.floor((xp - 95) / 15) + 11
    if xp < 5:  # TODO eradicate this abomination for something better
        return 1
    elif xp < 11:
        return 2
    elif xp < 18:
        return 3
    elif xp < 26:
        return 4
    elif xp < 35:
        return 5
    elif xp < 45:
        return 6
    elif xp < 56:
        return 7
    elif xp < 68:
        return 8
    elif xp < 81:
        return 9
    return 10


def getXPInLevel(xp: int) -> int:
    """Returns the XP the that a given amount would have left over"""
    if xp >= 95:
        return (xp - 95) % 15
    if xp < 5:  # TODO eradicate this abomination for something better
        return xp
    elif xp < 11:
        return xp - 5
    elif xp < 18:
        return xp - 11
    elif xp < 26:
        return xp - 18
    elif xp < 35:
        return xp - 26
    elif xp < 45:
        return xp - 35
    elif xp < 56:
        return xp - 45
    elif xp < 68:
        return xp - 56
    elif xp < 81:
        return xp - 68
    return xp - 81
# endregion


if __name__ == "__main__":
    play()
