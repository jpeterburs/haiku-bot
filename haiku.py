import syllables

def split_into_haiku(string):
  words = string.split()
  lines = [[], [], []]  # Use a list to store lines 1, 2, and 3

  syllable_count = 0
  for word in words:
    syllable_count += syllables.estimate(word)
    if syllable_count <= 5:
      lines[0].append(word)
    elif syllable_count <= 12:
      lines[1].append(word)
    else:
      lines[2].append(word)

  return [' '.join(line) for line in lines]

def _count_syllables(line):
  words = line.split()
  return sum(syllables.estimate(word) for word in words)

def is_haiku(lines):
  expected_syllables = [5, 7, 5]
  line_syllables = [_count_syllables(line) for line in lines]

  return line_syllables == expected_syllables