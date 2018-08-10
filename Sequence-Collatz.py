class RefValue(object):
    def __init__(self, val):
        self.val = val


def collatz(n, steps):
    while n > 1:
        steps.val += 1
        if n % 2 == 0:
            n //= 2
        else:
            n = 3 * n + 1
    return n


def collatz_r(n, steps):
    if n == 1:
        return 1
    steps.val += 1
    if n % 2 == 0:
        return collatz_r(n / 2, steps)
    else:
        return collatz_r(3 * n + 1, steps)


class TestCollatz(object):
    def common_assert(self, inp, expected):
        print("")
        steps = RefValue(0)
        r = collatz_r(inp, steps)
        print("steps = {}".format(steps.val))
        assert r == 1
        assert steps.val == expected

    def test_9(self):
        self.common_assert(9, 19)

    def test_12(self):
        self.common_assert(12, 9)

    def test_max(self):
        max_steps = 0
        starting_number_max_steps = 0
        for n in range(1, 100_000):
            steps = RefValue(0)
            r = collatz_r(n, steps)
            if steps.val > max_steps:
                max_steps = steps.val
                starting_number_max_steps = n
            assert r == 1
        assert starting_number_max_steps == 77_031
        assert max_steps == 350
