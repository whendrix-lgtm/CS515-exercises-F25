class Time:
  '''Class that represents some amount of time (hours, minutes, and seconds)'''
  def __init__(self, hours = 0, minutes = 0, seconds = 0):
    if hours >= 0:
      self.hr = hours
    else:
      self.hr = 0
    if minutes >= 0 and minutes <= 59:
      self.min = minutes
    else:
      self.min = 0
    if seconds >= 0 and seconds <= 59:
      self.sec = seconds
    else:
      self.sec = 0
  def __str__(self):
    ''' Returns time formatted as HH:MM:SS'''
    return f'{self.hr:0>2}:{self.min:0>2}:{self.sec:0>2}'
  def get_hours(self):
    return self.hr
  def set_hours(self, new_hours):
    if new_hours >= 0:
      self.hr = new_hours
  def get_minutes(self):
    return self.min
  def set_minutes(self, new_min):
    if new_min >= 0 and new_min <= 59:
      self.min = new_min
  def get_seconds(self):
    return self.sec
  def set_seconds(self, new_sec):
    if new_sec >= 0 and new_sec <= 59:
      self.sec = new_sec

t = Time() # Default time (00:00:00)
print(f'Default time:  {t}')
t2 = Time(12, 34, 56)
print(f'12 hours, 34 minutes, 56 seconds:  {t2}')
t3 = Time(1, 2, 3)
print(f'1 hours, 2 minutes, 3 seconds:  {t3}')
