import re

pattern = r'2?([013-9]+2)*[013-9]*'

while True:
  try:
    text = input('Enter an integer: ')
    x = int(text)
    if re.fullmatch(pattern, text):
      print(f"{text} doesn't contain consecutive 2's")
    else:
      print(f"{text} contains consecutive 2's")
  except ValueException:
    break

