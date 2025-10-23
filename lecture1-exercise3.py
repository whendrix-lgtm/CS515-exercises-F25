'''
Exercise:
  Prompt a user for their birth year and whether they have
  had a birthday this year, then calculate their age
  Interpret everything other than 'yes' as a "no"
  If birthday, age = 2025 - birth_year
  Otherwise, age = 2024 - birth_year
'''

year = int(input('What is your birth year? '))
birthday = str(input('Have you had a birthday this year? '))
if birthday == "yes":
  print('Your age is', 2025 - year)
else:
  print('Your age is', 2024 - year)
