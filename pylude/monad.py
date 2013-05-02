from applicative import Applicative
from function import curry

class Monad(Applicative):
  b = None

  def __init__(self, b, p):
    Applicative.__init__(self, lambda f: lambda a: b(lambda ff: b(lambda aa: p(lambda: ff(aa)))(a))(f), p)
    self.b = b

  def bind(self, f, a):
    return self.b(f)(a)

  def join(self, k):
    return self.bind(identity, k)

def __sequenceBind(f, a):
  r = []
  for i in a:
    r.extend(f(i))
  return r

sequenceMonad = Monad(curry(__sequenceBind), lambda k: [k()])

lambdaMonad = Monad(lambda f: lambda a: lambda t: f(a(t))(t), lambda k: lambda _: k())
