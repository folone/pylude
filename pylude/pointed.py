from functor import Functor, sequenceFunctor, lambdaFunctor
from function import curry


class Pointed(Functor):
    p = None

    def __init__(self, f, p):
        Functor.__init__(self, f)
        self.p = p

    def pure(self, a):
        return self.p(a)

sequencePointed = Pointed(curry(sequenceFunctor.fmap), lambda k: [k()])

lambdaPointed = Pointed(curry(lambdaFunctor.fmap), lambda k: lambda _: k())
