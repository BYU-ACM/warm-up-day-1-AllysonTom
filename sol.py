def Newtons_Method(func, func_prime, x_0, iters=100, tol=1e-5):
  """A direct implementation of Newton's Method
     (For sanity assume that func and func_prime define their own division correctly,
     that is, don't cast anything to a float)
     params: func: a function,
             fuc_prime: its direvative
             x_0: an itial guess (required)
             iters:number of iterations to cap too (optional, default 100)
             tol: acceptable distance from 0 (optional, default 1e-5)
     returns: a root(int) if found
              None(none-type) else
  """
  i = 1
  x1 = x_0 - func(x_0)/func_prime(x_0)
  while (i < iters):
    if (abs(x1 - x_0) > tol):
      i += 1
      x_0 = x1
      x1 = x_0 - func(x1)/func_prime(x1)
    else:
      return x1
"""
def func(x):
  return float(x**2) - 5.
def func_prime(x):
  return 2.*x
x_0 = -5.0
print Newtons_Method(func, func_prime, x_0)"""