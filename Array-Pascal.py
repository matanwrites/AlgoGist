def pascal(numRows):
    res = []
    for i in range(1, numRows + 1):
        r = []
        while len(r) < i:
            for n in range(i):
                if n == 0 or n == i - 1:
                    r.append(1)
                else:
                    r.append(prev[n-1] + prev[n])
        prev = r[:]
        res.append(prev)
    return res


def getRow(rowIndex):
    for i in range(0, rowIndex + 1 + 1):
        r = []
        while len(r) < i:
            for n in range(i):
                if n == 0 or n == i - 1:
                    r.append(1)
                else:
                    r.append(prev[n-1] + prev[n])
        prev = r[:]
    return r

class TestPascal(object):
    def common_assert(self, k, expected):
        r = pascal(k)
        assert r == expected

    def test_1(self):
        self.common_assert(1, [ getRow(0) ])

    def test_2(self):
        self.common_assert(2,[ getRow(0), getRow(1) ])

    def test_3(self):
        self.common_assert(3,[ getRow(0), getRow(1), getRow(2) ])


class TestGetRow(object):
    def common_assert(self, k, expected):
        r = getRow(k)
        assert r == expected

    def test_0(self):
        self.common_assert(0, [1])

    def test_1(self):
        self.common_assert(1, [1,1])

    def test_2(self):
        self.common_assert(2, [1, 2, 1])

    def test_3(self):
        self.common_assert(3, [1, 3, 3, 1])

    def test_4(self):
        self.common_assert(4, [1, 4, 6, 4, 1])

    def test_5(self):
        self.common_assert(5, [1, 5, 10, 10, 5, 1])
