import math
from time import sleep
import os


# region Main
def main():
    """The main function that initializes the project."""
    terminal_width = os.get_terminal_size().columns
    print("gsooA".center(terminal_width))
    sleep(0.5)
    print("Procedural Maths Game".center(terminal_width))
    sleep(0.5)
    print("By: Rin (BanaCubed)".center(terminal_width))
    sleep(0.5)
    print("-" * terminal_width)
    print("Press Enter to Start".center(terminal_width))
    input()
    clear()
    menu()
# endregion


# region Menu
def menu():
    """Renders the main menu."""
    render(
        "gsooA",
        "",
        "| Play   ",
        # "| Options",
        "| Exit   ",
        "|        "
    )

    while True:
        key = "".join(
            input(" " * (math.floor(os.get_terminal_size().columns/2) - 5) + "| > ").lower().split()
        )
        if key in [
            "play",
            "p",
            "start",
            "begin",
            "startgame",
            "begingame",
            "playgame",
        ]:
            break
        # elif key in [
        #     "options",
        #     "o",
        #     "settings",
        #     "optionsmenu",
        #     "settingsmenu",
        #     "gameoptions",
        #     "gameoptionsmenu",
        #     "gamesettings",
        #     "gamesettingsmenu",
        # ]:
        #     pass
        elif key in [
            "exit",
            "e",
            "quit",
            "exitgame",
            "quitgame",
            "close",
            "closegame",
            "q",
        ]:
            render(
                "gsooA",
                "",
                "Closing...",
                "",
            )
            sleep(1)
            exit()
        render(
            "gsooA",
            "",
            "Play",
            "Options",
            "Exit",
            "",
            "Invalid input",
            "Please try again",
            "",
            f"|{key}|",
        )
# endregion


# region Utils
def clear():
    """Clears the terminal."""
    os.system("cls" if os.name == "nt" else "clear")


def render(*text: str) -> None:
    """Renders centered text to the terminal."""
    clear()
    terminal_width = os.get_terminal_size().columns
    full_text = ""
    for line in text:
        full_text += line.center(terminal_width) + (
            "\n" if text.index(line) < text.__len__() - 1 else ""
        )
    print(full_text)
# endregion


if __name__ == "__main__":
    main()
