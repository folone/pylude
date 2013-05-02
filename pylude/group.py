import monoid


class Group(monoid.Monoid):
    def __init__(self, append, zero, inverse):
        monoid.Monoid.__init__(self, append, zero)
        self.inverse = inverse

    def invert(self, a):
        return self.inverse(a)


numAdditionGroup = monoid.Monoid(monoid.numAdditionMonoid.mappend,
                                 monoid.numAdditionMonoid.zero,
                                 lambda a: -a)

floatMultiplicationGroup = monoid.Monoid(
    monoid.numMultiplicationMonoid.mappend,
    monoid.numMultiplicationMonoid.zero,
    lambda a: 1. / a)
