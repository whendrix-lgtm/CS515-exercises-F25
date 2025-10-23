'''
  Find the two roots of a given quadratic function y = ax^2 + bx + c
'''

def get_left_root(a, b, c):
  return (-b - (b ** 2 - 4 * a * c) ** 0.5) / (2*a)

def get_right_root(a, b, c):
  return (-b + (b ** 2 - 4 * a * c) ** 0.5) / (2*a)

a = float(input("Enter a: "))
b = float(input("Enter b: "))
c = float(input("Enter c: "))

print("The roots of that equation are ", get_left_root(a, b, c), "and", get_right_root(a, b, c))
