import os


# region Clear
def clear():
    """Clears the terminal."""
    os.system("cls" if os.name == "nt" else "clear")
# endregion


# region Render
def render(*text: str) -> None:
    """Renders formatted text to the terminal."""
    clear()
    full_text = ""
    for line in text:
        full_text += (
            "     "
        ) + line + (
            "\n" if text.index(line) < text.__len__() - 1 else ""
        )
    print(full_text)
# endregion
