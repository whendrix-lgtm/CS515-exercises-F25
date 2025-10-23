# Pig Latin translator

def piglatin(word):
  vowels = 'aeiou'
  for i in range(len(word)):
    if word[i] in vowels:
      break
  else:
    i = 0
  return word[i:] + word[:i] + 'ay'

english = input('Enter a sentence to translate to Pig Latin: ')
pig = []
for word in english.split():
  pig.append(piglatin(word))
print(f'{english}\ntranslates as:\n{' '.join(pig)}\nin Pig Latin')
