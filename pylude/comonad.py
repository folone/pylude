from copointed import Copointed
from function import identity


class Comonad(Copointed):
    cob = None

    def __init__(self, cop, ext):
        Copointed.__init__(self, lambda k: ext(cop(lambda: k)), cop)
        self.cop = cop
        self.ext = ext

    def extend(self, f, wa):
        return self.ext(f)(wa)

    def duplicate(self, wa):
        return self.extend(identity, wa)

    def extract(self, wa):
        return self.cop(wa)

lambdaComonad = Comonad(lambda _: lambda a: a(),
                        lambda f: lambda a: lambda t: lambda: f(a(t))(t))

