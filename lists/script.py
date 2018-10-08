from galaxy import load_ship

from galaxy import prompt
# 3...2...1...
# blast off!!
load_ship()

moon_count = 0

print()
print("Our solar system contains 9 different planets. Here they are in order:")
print("Mercury, Venus, Earth, Mars, Jupiter, Saturn, Uranus, Neptune, Pluto.")
# let's see how many moons we can explore!
prompt(moon_count)
