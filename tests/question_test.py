from math import prod
from questions import Question, AdditionQuestion, SubtractionQuestion, MultiplicationQuestion
from state import unstableState


# region Generic
class TestGenericQuestion:
    def test_generic_initialisation(self):
        q = Question()
        assert q.seed == unstableState["seed"]
        assert q.level == unstableState["level"]
        assert q.values == []
        assert q.answer == 0

    def test_generic_verifyAnswer(self):
        q = Question()
        assert q.verifyAnswer("0") is True
# endregion


# region Addition
class TestAdditionQuestion:
    def test_addition_initialisation(self):
        q = AdditionQuestion(1, 1)
        assert q.seed == 1
        assert q.level == 1

    def test_addition_edge_cases(self):
        # First argument/seed has no effect on error throwing
        try:
            AdditionQuestion(0, -1)
            assert False  # Should error, min level is 1
        except ValueError:
            assert True
        try:
            AdditionQuestion(0, 0)
            assert False  # Should error
        except ValueError:
            assert True
        try:
            AdditionQuestion(0, 1)
            assert True  # Shouldn't error, at minimum level
        except ValueError:
            assert False
        try:
            AdditionQuestion(0, 2)
            assert True  # Shouldn't error
        except ValueError:
            assert False

    def test_addition_verifyAnswer(self):
        for i in range(20):
            q = AdditionQuestion(1, max(i, 1))
            assert q.verifyAnswer(str(sum(q.values)))
# endregion


# region Subtraction
class TestSubtractionQuestion:
    def test_subtraction_initialisation(self):
        q = SubtractionQuestion(1, 2)
        assert q.seed == 1
        assert q.level == 2

    def test_subtraction_edge_cases(self):
        # First argument/seed has no effect on error throwing
        try:
            SubtractionQuestion(0, -1)
            assert False  # Should error, min level is 2
        except ValueError:
            assert True
        try:
            SubtractionQuestion(0, 0)
            assert False  # Should error
        except ValueError:
            assert True
        try:
            SubtractionQuestion(0, 1)
            assert False  # Should error
        except ValueError:
            assert True
        try:
            SubtractionQuestion(0, 2)
            assert True  # Shouldn't error, at minimum level
        except ValueError:
            assert False
        try:
            SubtractionQuestion(0, 3)
            assert True  # Shouldn't error
        except ValueError:
            assert False

    def test_subtraction_verifyAnswer(self):
        for i in range(20):
            q = SubtractionQuestion(1, max(i, 2))
            vals = q.values
            ans = vals[0]
            vals.pop(0)
            for val in vals:
                ans -= val
            assert q.verifyAnswer(str(ans))
# endregion


# region Multiplication
class TestMultiplicationQuestion:
    def test_multiplication_initialisation(self):
        q = MultiplicationQuestion(1, 3)
        assert q.seed == 1
        assert q.level == 3

    def test_multiplication_edge_cases(self):
        # First argument/seed has no effect on error throwing
        try:
            MultiplicationQuestion(0, -1)
            assert False  # Should error, min level is 3
        except ValueError:
            assert True
        try:
            MultiplicationQuestion(0, 2)
            assert False  # Should error
        except ValueError:
            assert True
        try:
            MultiplicationQuestion(0, 3)
            assert True  # Shouldn't error, at minimum level
        except ValueError:
            assert False
        try:
            MultiplicationQuestion(0, 4)
            assert True  # Shouldn't error
        except ValueError:
            assert False

    def test_multiplication_verifyAnswer(self):
        for i in range(20):
            q = MultiplicationQuestion(1, max(i, 3))
            assert q.verifyAnswer(str(prod(q.values)))
# endregion
