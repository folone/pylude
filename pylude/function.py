uncurry = lambda f: lambda a: f(a[0])(a[1])

curry = lambda f: lambda a: lambda b: f(a, b)

identity = lambda a: a

const = lambda a: lambda b: a

