'''
  Recursive is_palindrome function that accepts a string
  and returns whether it is a palindrome
  Examples:
    huh
    noon
    racecar
'''

def is_palindrome(str):
  if len(str) <= 1:
    return True
  elif str[0].lower() != str[-1].lower():
    return False
  else:
    return is_palindrome(str[1:-1])

str = input("Enter a string: ")
if is_palindrome(str):
  print("That is a palindrome")
else:
  print('That is not a palindrome')
