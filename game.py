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
        "seed": random.randint(0, 100000) if seed is None else seed,
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
            f"| lv. {unstableState["level"]}{
                " ★" if
                stableState.value["bestLevel"] != 0 and
                unstableState["level"] > stableState.value["bestLevel"] else ""
                }",
            f"| hp. {"@" * unstableState["hp"]}",
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
            })
        else:
            unstableState.update({
                "hp": unstableState["hp"] - 1
            })
            if unstableState["hp"] <= 0:
                lose()
                break
# endregion


# region Lose
def lose():
    unstableState.update({"running": False})
    stableState.setValue("totalScore", stableState.value["totalScore"] + unstableState["score"])
    stableState.setValue("bestScore", max(stableState.value["bestScore"], unstableState["score"]))
    stableState.setValue("bestLevel", max(stableState.value["bestLevel"], unstableState["level"]))
# endregion


if __name__ == "__main__":
    play()
