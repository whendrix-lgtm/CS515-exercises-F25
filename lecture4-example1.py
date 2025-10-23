'''
  Estimate pi using random numbers
'''
import random
import math

count = 0
for i in range(100000):
  x = random.uniform(0, 1)
  y = random.uniform(0, 1)
  dist = (x * x + y * y) ** 0.5
  if dist <= 1.0: # should happen pi/4 % of the time
    count += 1

approx_pi = count / 100000 * 4
print(f'Pi is approx {approx_pi}')
print(f'pi = {math.pi}')
