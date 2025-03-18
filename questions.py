import math

from jinja2 import Undefined
from prng import prng
from state import unstableState


# region Generic
class Question:
    """
    A generic class for any question type.

    Initialization Args:
    - `seed`: The seed used to generate the question
    - `level`: The level of the question used to determine the difficulty

    Instance Properties:
    - `seed`: The seed used to generate the question
    - `level`: The level at which the question was generated
    - `answer`: The correct answer to the question
    - `values`:  list of values used to calculate the question's answer and stringification

    Static Properties:
    - `minLevel`: The minimum level that this question type can appear at

    Methods:
    - `verifyAnswer(answer: str) -> bool`: Verifies whether a given answer is correct
    """
    seed: int
    """
    The seed used to generate the question
    """
    level: int
    """
    The level at which the question was generated
    """
    values: list[float]
    """
    A list of values used to calculate the question's answer and stringification
    """
    answer: float
    """
    The correct answer to the question
    """
    minLevel: int
    """
    `static`
    The minimum level that this question type can appear at
    """

    def __init__(self, seed: int, level: int):
        self.seed = seed if seed is not Undefined else unstableState.seed
        self.level = level if level is not Undefined else unstableState.level

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
            _answer = float(answer)
        except ValueError:
            raise ValueError("Answer must be a number")

        return self.answer == _answer

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

    Instance Properties:
    - `seed`: The seed used to generate the question
    - `level`: The level at which the question was generated
    - `answer`: The correct answer to the question
    - `values`:  list of values used to calculate the question's answer and stringification

    Static Properties:
    - `minLevel`: The minimum level that this question type can appear at

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
        return math.ceil((1.25 ** level) * 7)

    def __str__(self):
        text = ""
        for i in range(len(self.values)):
            text += f"{self.values[i]}"
            if i < len(self.values) - 1:
                text += " + "
        return text + " = ?"
# endregion


# region Collection
questionTypes = [AdditionQuestion]
"""
A list of all question types.

If a list of types is needed, use `gatherQuestionTypes(level: int) -> list` instead.
"""


def gatherQuestionTypes(level: int) -> list:
    """
    Returns a list of all question types possible at a given level

    Args:
    - `level`
    """
    types = []
    for questionType in questionTypes:
        if questionType.minLevel <= level:
            types.append(questionType)
    return types
# endregion
