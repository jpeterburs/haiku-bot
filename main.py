import discord
import syllables
import os

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

class Client(discord.Client):
  async def on_message(self, message):
    if message.author.bot:
      return

    poem = split_into_haiku(message.content.replace('\n', ' '))

    if is_haiku(poem):
      haiku = '\n'.join(poem) + '\n'

      reply = await message.reply(haiku + '\n*Beep noop! Ich halte Ausschau nach versehentlichen Haikus. Manchmal mache ich Fehler.*')
      await reply.add_reaction('⬆️')
      await reply.add_reaction('⬇️')

intents = discord.Intents.default()
intents.message_content = True

client = Client(intents = intents)
client.run(os.environ['TOKEN'])