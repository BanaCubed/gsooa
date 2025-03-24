from state import unstableState


# region PRNG
def prng(seed: int | None = None, min: int = 0, max: int = 1) -> float:
    """
    `prng()` takes an optional input seed, defaulting to `unstableState["seed"]`.
    The function then returns a pseudo-random number between 0 and 1.

    Args:
    - `seed`: The seed to use for the PRNG. If not provided, the default seed will be used.
    - `min`: The minimum value to return.
    - `max`: The maximum value to return.

    Returns:
    - A pseudo-random number between 0 and 1.

    The PRNG uses the linear congruential generator (LCG) algorithm.

    Sources:
    - [Wikipedia - LCG](https://en.wikipedia.org/wiki/Linear_congruential_generator)
    """
    # Setting up the seed value to be slightly less predictable
    x: int = (seed if seed is not None else unstableState["seed"]) ^ unstableState["prngRuns"]
    x = (x << 13) * x

    x = lcg(x)

    # Update the PRNG runs counter
    unstableState.update({"prngRuns": unstableState["prngRuns"] + 1})

    # Return the output value
    return x / 2**64 * (max - min) + min
# endregion


# region LCG
def lcg(x: int, a: int = 6364136223846793005, c: int = 1442695040888963407, m: int = 2**64) -> int:
    """
    Applies the Linear Congruential Generator (LCG) algorithm using MMIX parameters by default.

    Args:
    - `x`: The input seed value
    - `a`: Multiplier constant
    - `c`: Increment constant
    - `m`: Modulus constant

    Returns:
    - The next value in the LCG sequence

    The LCG is defined by the recurrence relation:
    `R = (a * x + c) % m`

    Here `x` is the first argument.
    `a`, `c`, and `m` are optional arguments.
    `R` is the returned value.

    The default constants are taken from MMIX by Donald Knuth.
    ```python
    a = 6364136223846793005  # Multiplier
    c = 1442695040888963407  # Increment
    m = 2**64  # Modulus
    ```

    Sources:
    - [Wikipedia - LCG](https://en.wikipedia.org/wiki/Linear_congruential_generator)
    - [Donald Knuth - MMIX](http://mmix.cs.hm.edu/doc/mmix-doc.pdf)
    """
    return (a * x + c) % m
# endregion
