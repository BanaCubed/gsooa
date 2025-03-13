from app.prng import prng


class TestPRNG:
    def test_prng_seed(self):
        assert prng() == prng(1)
