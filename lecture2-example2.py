'''
  Prompt the user for two integers, m and n,
  and print a table of the function f(x) = x^2
  for all values from m up to (but not including) n
'''

m = int(input('Enter start value: '))
n = int(input('Enter ending value: '))

print('    x      x^2')
for i in range(m, n):
  print(f'{i:>5} {i*i:>8}')
