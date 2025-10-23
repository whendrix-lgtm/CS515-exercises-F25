'''
  Script that rolls dice and outputs the total

  User specifies dice in the format NdK, where
   N = # of dice
   K = # of sides
'''
import random

# Prompt user to enter dice
dice = input("Enter dice to roll in the format NdK: ")

# Calculate # of dice and sides
parts = dice.split('d')
num = int(parts[0])
size = int(parts[1])

# Roll dice
total = 0
for i in range(num):
  roll = random.randint(1, size)
  print(roll)
  total += roll

# Calculate total and print
print(f'Total = {total}')

