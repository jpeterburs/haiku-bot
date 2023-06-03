import interactions
import syllables
import os

client = interactions.Client(token = os.environ['TOKEN'], intents = interactions.Intents.DEFAULT | interactions.Intents.GUILD_MESSAGE_CONTENT)

def split_into_haiku(string):
  words = string.split()
  haiku = []
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

def count_syllables(line):
  words = line.split()
  return sum(syllables.estimate(word) for word in words)

def is_haiku(lines):
  expected_syllables = [5, 7, 5]
  line_syllables = [count_syllables(line) for line in lines]

  return line_syllables == expected_syllables


@client.event
async def on_message_create(message):
  if message.author.bot:
    return

  poem = split_into_haiku(message.content.replace('\n', ' '))

  if is_haiku(poem):
    haiku = '\n'.join(poem) + '\n'

    reply = await message.reply(haiku + '\n*Beep noop! Ich halte Ausschau nach versehentlichen Haikus. Manchmal mache ich Fehler.*')
    await reply.create_reaction('⬆️')
    await reply.create_reaction('⬇️')

client.start()