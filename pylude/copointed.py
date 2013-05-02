from functor import Functor


class Copointed(Functor):
    f = None

    def __init__(self, f, extr):
        Functor.__init__(self, f)
        self.extr = extr

    def extract(self, fa):
        return self.extr(fa)
