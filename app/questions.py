# region Generic
class Question:
    """
    A generic class for any question type.

    Initialization takes the following properties:
    - `seed`: The seed used to generate the question
    - `level`: The level of the question

    A question has the following properties:
    - `answer`: The correct answer to the question
    - `values`: A list of values that are used within rendering the question
    - `seed`: The seed used to generate the question
    - `level`: The level of the question
    """
    def __init__(self, seed: int, level: int):
        self.seed = seed
        self.level = level

    def generate(self):
        pass

    def __str__(self):
        return f"Unset Question Type - Seed: {self.seed} - Level: {self.level}"
# endregion


print(Question(1, 1))
