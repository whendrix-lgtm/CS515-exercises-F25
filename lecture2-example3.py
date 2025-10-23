'''
  Print top 20 girl and boy baby names from babynames.txt
'''

file = open('babynames.txt')

print('Top 20 girl names:')
for i in range(20):
  print(file.readline(), end='')

for i in range(980):
  file.readline()

print('Top 20 boy names:')
for i in range(20):
  print(file.readline(), end='')

file.close()
