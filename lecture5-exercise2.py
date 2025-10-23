story = '''In the year 3099, Earth was entirely covered in chrome,
thanks to the Great Reflective Revolution of 2872. Humanity had evolved
beyond needing food, sleep, or emotional depth, replacing all biological
functions with quantum spaghetti—threads of hyperintelligent pasta that
regulated metabolism and sent Tweets to the moon. President Zlorb, a
sentient vending machine with a knack for interpretive dance, ruled the
Unified Galactic Condo with an iron push-button. His cabinet included a
disgruntled AI toaster and a raccoon that had achieved Nirvana after
licking a USB port. Deep within the Crust Nebula, a spaceship made
entirely of recycled hubcaps and forgotten dreams drifted aimlessly.
Its crew, genetically engineered from the DNA of Shakespeare and various
mid-2000s pop stars, spoke only in rhymed couplets and obscure memes.
Their mission was to retrieve the Sacred Crouton, an ancient artifact
rumored to grant unlimited Wi-Fi and the ability to taste colors.
Unfortunately, they were being hunted by the dreaded Space Bureaucrats,
beings of pure paperwork who could slow any plotline to a crawl with
just one poorly formatted form. Meanwhile, on Jupiter’s least popular moon,
Dennis, a rebel faction known as The Rejected Plot Devices plotted to
rewrite the laws of physics using a sentient screenplay written during a
solar flare. Their leader, Captain Hologram McBeardface, had a mechanical
arm that dispensed cold brew and quotes from outdated self-help books.
As the galactic tension rose to a medium simmer, only one thing was certain:
the final battle would be fought in interpretive dance... and everyone had
forgotten how to moonwalk.'''

# Proper nouns:
# * Great Reflective Revolution
# * President Zlorb
# * Unified Galactic Condo
# * Crust Nebula
# * Sacred Crouton
# * Wi-Fi
# * Space Bureaucrats
# * The Rejected Plot Devices
# * Captain Hologram

import re

def get_all_matches(pattern, text):
  out = []
  res = re.search(pattern, text)
  while res:
    out.append(text[res.start():res.end()])
    text = text[res.end():]
    res = re.search(pattern, text)
  return out

pattern = r'[A-Z][a-z]+([ -][A-Z][a-z]+)+'
matches = get_all_matches(pattern, story)
for match in matches:
  print(match)

