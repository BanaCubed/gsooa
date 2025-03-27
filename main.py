from time import sleep
import os

from game import play
from render import clear, render


# region Main
def main():
    """The main function that initializes the project."""
    terminal_width = os.get_terminal_size().columns
    print("gsooA".center(terminal_width))
    sleep(0.5)
    print("Procedural Maths Game".center(terminal_width))
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
        "| play",
        # "| options",
        "| exit",
        "|"
    )

    while True:
        key = "".join(
            input("     | > ").lower().split()
        )
        if key in [
            "play",
            "p",
            "start",
            "begin",
            "startgame",
            "begingame",
            "playgame",
            "game",
        ]:
            play()
            render(
                "gsooA",
                "",
                "| play",
                # "| options",
                "| exit",
                "|",
            )
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
            "x",
        ]:
            render(
                "gsooA",
                "",
                "Closing...",
                "",
            )
            sleep(1)
            exit()
        else:
            render(
                "gsooA",
                "",
                "| play",
                # "| options",
                "| exit",
                "|",
                "| input could not be interpereted",
                "| try again",
                "|",
            )
# endregion


if __name__ == "__main__":
    main()
