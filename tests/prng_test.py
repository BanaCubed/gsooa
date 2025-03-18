from prng import prng


class TestPRNG:
    def test_prng_seed_consistency(self):
        assert prng(1) == 0.6674361971562441

    def test_prng_seed_differing(self):
        assert prng(1) != prng(1)

    def test_prng_seed_consistency_with_min_max(self):
        assert prng(1, 0, 10) == 2.566637394341944

    def test_prng_seed_differing_with_min_max(self):
        assert prng(1, 0, 10) != prng(1, 0, 10)
