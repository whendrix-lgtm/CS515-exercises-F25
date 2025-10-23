'''
Example:
  Prompts the user for the temperature (in Fahrenheit)
  and outputs the phase of water (at atmospheric pressure)
'''
temp = int(input('What is the temperature (in F)? '))
if temp < 32:
  print('Water is solid.')
elif temp == 32:
  print('Water is solid and liquid.')
elif temp < 212:
  print('Water is liquid.')
elif temp == 212:
  print('Water is liquid and gas.')
else:
  print('Water is gas.')

  
