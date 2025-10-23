class Complex:
  '''
  Class representing a complex number (a + bi)
  '''
  def __init__(self, re = 0, im = 0):
    '''
    Initializes number to (re) + (im)i
    0 + 0i, by default
    '''
    self.re = re
    self.im = im
  def add(self, other_complex):
    '''
    Adds the given complex number to this one
    Returns the result
    '''
    re = self.re + other_complex.re
    im = self.im + other_complex.im
    return Complex(re, im)
  def multiply(self, other):
    '''
    Multiplies this complex number by another
    Returns the result
    '''
    new_re = self.re * other.re - self.im * other.im
    new_im = self.re * other.im + self.im * other.re
    return Complex(new_re, new_im)
  def __str__(self):
    return f'{self.re}+{self.im}i'
  #Add operator overloads for + and *


# Test cases
x = Complex(5, 10)
y = Complex(5, -10)
print(f'{x} + {y} = {x + y}') # 10 + 0i
print(f'{x} * {y} = {x * y}') # 125 + 0i
print(f'{x} * ({x} + {y}) = {x * (x+y)}') # 50 + 100i
