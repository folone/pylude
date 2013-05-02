import semigroup


class Monoid(semigroup.Semigroup):
    def __init__(self, append, zero):
        semigroup.Semigroup.__init__(self, append)
        self.zero = zero

    def zero(self):
        return self.zero

numAdditionMonoid = Monoid(semigroup.numAdditionSemigroup.mappend, 0)
numMultiplicationMonoid = Monoid(semigroup.numMultiplicationSemigroup.mappend,
                                 1)

stringMonoid = Monoid(semigroup.stringSemigroup.mappend, "")
sequenceMonoid = Monoid(semigroup.sequenceSemigroup.mappend, [])
