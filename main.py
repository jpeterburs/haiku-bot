import discord
import interactions
import os

from haiku import split_into_haiku, is_haiku

client = interactions.Client(token = os.environ['TOKEN'], intents = interactions.Intents.DEFAULT | interactions.Intents.GUILD_MESSAGE_CONTENT)

@client.command(name = 'invite', description = f'Lade {client.me.name} auf deinen eigenen Server ein!')
async def invite_command(ctx: interactions.CommandContext):
  permissions = discord.Permissions()
  permissions.update(read_messages=True, send_messages=True, add_reactions = True)

  invite_link = discord.utils.oauth_url(client.me.id, permissions=permissions)
  await ctx.send(f'➡️ {invite_link}')

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