import discord
import syllables
import os

haiku_form = [5, 7, 5]

class Client(discord.Client):
  async def on_message(self, message):
    if message.author.bot:
      return

    syl_count = 0
    offset = 0
    i = 0
    haiku = []

    for syl_per_line in haiku_form:
      line = []

      if i == 0:
        words = message.content.split()
      else:
        words = message.content.split()[(offset - i):]

      for word in words:
        syl_count += syllables.estimate(word)
        line.append(word)

        if syl_count == syl_per_line:
          syl_count = 0
          haiku.append(line)
          break
        elif syl_count > syl_per_line:
          return

      offset += syl_per_line
      i += 1

    reply = ''
    for ln in haiku:
      reply += ' '.join(ln) + '\n'

    await message.reply(reply + '\n*Beep noop! Ich halte Ausschau nach versehentlichen Haikus. Manchmal mache ich Fehler.*')

intents = discord.Intents.default()
intents.message_content = True

client = Client(intents=intents)
client.run(os.environ['TOKEN'])