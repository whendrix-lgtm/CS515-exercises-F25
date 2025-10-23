'''
  Write a hypotenuse function that accepts the length of
  two sides of a right triangle (a and b) and computes
  the length of the hypotenuse using the Pythagorean
  Theorem (a^2 + b^2 = c^2)
'''
# Define hypotenuse here
def hypotenuse(a, b):
  return (a ** 2 + b ** 2) ** 0.5

# Test case 1
print(f'The hypotenuse of a 1,1 triangle is {hypotenuse(1,1)}')

# Test case 2
print(f'The hypotenuse of a 3,4 triangle is {hypotenuse(3,4)}')

# Test case 3
print(f'The hypotenuse of a 5,12 triangle is {hypotenuse(5,12)}')
