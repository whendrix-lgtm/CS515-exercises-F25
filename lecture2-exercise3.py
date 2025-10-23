'''
  Prompts the user for a file name, then multiple lines of text
  Writes all lines of text to the given file until the user
  enters a blank line (enter twice)
'''

a = input('Enter the file name: ')
file = open(a, 'w')
print('Start typing: ')
line = input()
while line != '':
  file.write(line + '\n')
  line = input()  

file.close()
