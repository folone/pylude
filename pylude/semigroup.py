class Semigroup(object):
    def __init__(self, append):
        self.append = append

    def mappend(self, a, b):
        return self.append(a, b)

numAdditionSemigroup = Semigroup(lambda i, j: i + j)
numMultiplicationSemigroup = Semigroup(lambda i, j: i * j)

stringSemigroup = numAdditionSemigroup  # Courtesy of ducktyping
sequenceSemigroup = numAdditionSemigroup  # Same here
