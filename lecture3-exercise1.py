'''
  Script that extracts various strings from the sentence
  "The quick brown fox jumps over the lazy dog"
'''

sent = "The quick brown fox jumps over the lazy dog"

# the lazy dog
print('"' + sent[31:] + '"')

# abc
print(f'"{sent[36] + sent[10] + sent[7]}"')

# revo
print(f'"{sent[29:25:-1]}"')
