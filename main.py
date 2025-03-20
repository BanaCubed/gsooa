from time import sleep
import os


# region Main
def main():
    print("Hello, World!")
    sleep(1)
    clear()
    sleep(1)
    main()
# endregion


# region Utils
def clear():
    os.system('cls' if os.name == 'nt' else 'clear')
# endregion


main()
