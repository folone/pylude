class Functor:
  f = None

  def __init__(self, f):
    self.f = f

  def fmap(self, k, a):
    return self.f(k)(a)
    
  def flip(self, f):
    return lambda a: self.fmap(lambda k: k(a), f)

sequenceFunctor = Functor(lambda f: lambda a: map(f, a))

lambdaFunctor = Functor(lambda f: lambda g: lambda x: f(g(x)))
