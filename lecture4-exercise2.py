'''
  Switch class
    Can be on or off (default on)
  Methods:
    turn_on
    turn_off
    flip
    is_on
  Can be printed using print()
    format:  Switch (on/off)
'''
class Switch:
  def __init__(self):
    self.status = 'off'
  def turn_on(self):
    self.status = 'on'
  def turn_off(self):
    self.status = 'off'
  def flip(self):
    if self.status == 'on':
      self.status = 'off'
    elif self.status == 'off':
      self.status = 'on'
  def is_on(self):
    return self.status == 'on'
  def __str__(self):
    return f'Switch ({self.status})'


# Testing code for Switch class
if __name__ == '__main__':
  test = Switch()
  print(f'Default switch: {test}')

  test.turn_on()
  print(f'On:  {test}')
  test.turn_on()
  print(f'On:  {test}')
  test.turn_off()
  print(f'Off:  {test}')
  test.turn_off()
  print(f'Off:  {test}')

  test.flip()
  print(f'On:  {test}')
  test.flip()
  print(f'Off:  {test}')

  if test.is_on():
    print('The switch is on (ERROR!)')
  else:
    print('The switch is off (CORRECT)')
    
  test.flip()
  if test.is_on():
    print('The switch is on (CORRECT)')
  else:
    print('The switch is off (ERROR!)')
