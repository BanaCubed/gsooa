import math
from app.prng import prng


# region Generic
class Question:
    """
    A generic class for any question type.

    Initialization Args:
    - `seed`: The seed used to generate the question
    - `level`: The level of the question

    Properties:
    - `answer`: The correct answer to the question
    - `values`: A list of values that are used within rendering the question
    - `seed`: The seed used to generate the question
    - `level`: The level of the question

    Methods:
    - `verifyAnswer(answer: str) -> bool`: Verifies whether a given answer is correct
    """
    seed: int
    level: int
    values: list[float]
    answer: float

    def __init__(self, seed: int, level: int):
        self.seed = seed
        self.level = level

        self.values = []
        self.answer = 0

    def verifyAnswer(self, answer: str) -> bool:
        """
        Verifies whether a given answer is correct.

        Args:
            `answer`: The answer to the question

        Returns:
            `bool`: Whether the answer is correct
        """
        try:
            float(answer)
        except ValueError:
            raise ValueError("Answer must be a number")

        return self.answer == answer

    def __str__(self):
        return f"Unset Question Type - Seed: {self.seed} - Level: {self.level}"
# endregion


# region Addition
class AdditionQuestion(Question):
    """
    A class for addition questions.

    Initialization Args:
    - `seed`: The seed used to generate the question
    - `level`: The level of the question

    Properties:
    - `answer`: The correct answer to the question
    - `values`: A list of values that are used within rendering the question
    - `seed`: The seed used to generate the question
    - `level`: The level of the question

    Public Methods:
    - `verifyAnswer(answer: str) -> bool`: Verifies whether a given answer is correct

    Static Methods:
    - `minValue(level: int) -> int`: Returns the minimum value for a given level
    - `maxValue(level: int) -> int`: Returns the maximum value for a given level
    """
    def __init__(self, seed: int, level: int):
        super().__init__(seed, level)

        self.values = [
            math.floor(prng(
                seed,
                self.minValue(level),
                self.maxValue(level)
            )) for _ in range(2)
        ]
        self.answer = sum(self.values)

    @staticmethod
    def minValue(level: int) -> int:
        """
        Returns the minimum value for a given level.

        Args:
            `level`: The level of the question

        Returns:
            The minimum value for the given level
        """
        if level < 0:
            raise ValueError("Level cannot be below 0")
        return 0 if level >= 3 else 1

    @staticmethod
    def maxValue(level: int) -> int:
        """
        Returns the maximum value for a given level.

        Args:
            `level`: The level of the question

        Returns:
            The maximum value for the given level
        """
        if level < 0:
            raise ValueError("Level cannot be below 0")
        return math.ceil((1.25 ** level) * 10)

    def __str__(self):
        text = ""
        for i in range(len(self.values)):
            text += f"{self.values[i]}"
            if i < len(self.values) - 1:
                text += " + "
        return text + " = ?"
# endregion


print(AdditionQuestion(1, 1))
