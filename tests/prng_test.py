from prng import prng, lcg


# region PRNG Tests
class TestPRNG:
    def test_prng_seed_consistency(self):
        assert prng(1) == 0.6674361971562441

    def test_prng_same_seed_differing(self):
        assert prng(1) != prng(1)

    def test_prng_seed_consistency_with_min_max(self):
        assert prng(1, 0, 10) == 2.566637394341944

    def test_prng_same_seed_differing_with_min_max(self):
        assert prng(1, 0, 10) != prng(1, 0, 10)
# endregion


# region LCG Tests
class TestLCG:
    def test_lcg_x_consistency(self):
        assert lcg(1) == 7806831264735756412

    def test_lcg_same_x_nondiffering(self):
        assert lcg(1) == lcg(1)

    def test_lcg_differing_x_differing(self):
        assert lcg(1) != lcg(2)
# endregion
