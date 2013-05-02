from pointed import Pointed, sequencePointed, lambdaPointed
from function import curry

class Applicative(Pointed):
  ap = None

  def __init__(self, ap, p):
    Pointed.__init__(self, lambda k: ap(p(lambda: k)), p)
    self.ap = ap

  def apply(self, f, a):
    return self.ap(f)(a)

def __sequenceApply(k, f):
  r = []
  for i in k:
    for j in f:
      r.append(i(j))
  return r

sequenceApplicative = Applicative(curry(__sequenceApply), sequencePointed.pure)

lambdaApplicative = Applicative(lambda f: lambda a: lambda t: f(t)(a(t)), lambdaPointed.pure)
