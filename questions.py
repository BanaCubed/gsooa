import math

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

    def __init__(self, seed: int | None = None, level: int | None = None):
        self.seed = seed if seed is not None else unstableState["seed"]
        self.level = level if level is not None else unstableState["level"]

        self.values = []
        self.answer = 0

    def verifyAnswer(self, answer: str) -> bool:
        """
        Verifies whether a given answer is correct.

        Args:
        - `answer`: The answer to the question

        Returns:
        - `bool`: Whether the answer is correct
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
    minLevel = 1

    def __init__(self, seed: int | None = None, level: int | None = None):
        super().__init__(seed, level)

        self.values = [
            math.floor(prng(  # "x if x is not None else y" is required here to avoid type issues
                seed if seed is not None else unstableState["seed"],
                self.minValue(level if level is not None else unstableState["level"]),
                self.maxValue(level if level is not None else unstableState["level"])
            )) for _ in range(2)
        ]
        self.answer = sum(self.values)

    @staticmethod
    def minValue(level: int) -> int:
        """
        Returns the minimum value for a given level.

        Args:
        - `level`: The level of the question

        Returns:
        - The minimum value for the given level
        """
        if level < AdditionQuestion.minLevel:
            raise ValueError(f"Level cannot be below {AdditionQuestion.minLevel}")
        return 0 if level >= 3 else 1

    @staticmethod
    def maxValue(level: int) -> int:
        """
        Returns the maximum value for a given level.

        Args:
        - `level`: The level of the question

        Returns:
        - The maximum value for the given level
        """
        if level < AdditionQuestion.minLevel:
            raise ValueError(f"Level cannot be below {AdditionQuestion.minLevel}")
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
questionTypes: list[type[Question]] = [AdditionQuestion]
"""
A list of all question types.

If a list of types is needed, use `gatherQuestionTypes(level: int) -> list` instead.
"""


def gatherQuestionTypes(level: int) -> list[type[Question]]:
    """
    Returns a list of all question classes allowed at a given level

    Args:
    - `level`: The level to check with minLevel

    Returns:
    - A list of all question classes allowed at the given level
    """
    types = []
    for questionType in questionTypes:
        if questionType.minLevel <= level:
            types.append(questionType)
    return types
# endregion


# region Generation
def generateQuestion(seed: int | None = None, level: int | None = None) -> Question:
    """
    Generates a question of a given level.

    Args:
    - `seed`: The seed used to generate the question
    - `level`: The level of the question

    Returns:
    - A question of the given level
    """
    seed = seed if seed is not None else unstableState["seed"]
    level = level if level is not None else unstableState["level"]
    types = gatherQuestionTypes(level)
    if len(types) == 0:
        # May be helpful to show the level for future debugging
        raise ValueError(f"No question types found for level {level}")
    # TODO add error handling
    questionType = types[math.floor(prng(seed, 0, len(types)))]
    question = questionType(seed, level)
    return question
# endregion


for i in range(10):
    print(generateQuestion(1, i+1))
