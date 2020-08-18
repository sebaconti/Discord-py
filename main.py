import discord
from discord.ext import commands
import os
from multi_server import *

spam_header = '¡El rico spam viene!'
spam_var = 'El spam for you:\nhttps://www.youtube.com/channel/UCOiUjXdZ_kXJNXXjwtEsiQg'
##spam_header = '¡El rico spam viene!'
embed = discord.Embed(color= discord.Color.blue(),title= "Spam Bot",type= "rich",author= "<@689534437356077184>",description= "The spammer bot is a bot for spam")
embed.add_field(name="Consequences",value="This bot can cause a lot of spam")
embed.set_author(name = "@sebaconti19#3194")

stop = False
coso = True

#spam_var = discord.Guild()
second_admin = ''

#bot = commands.Bot('', "This is a spammer bot")#bot('', "This is a spammer bot")
client = discord.Client()
bot = commands.Bot(command_prefix='', description="This is a Helper Bot")

spam_count = 0
terminado = True

@bot.command()
async def Spam(ctx, numero = 1):
  await spam(ctx, numero)

@bot.command()
async def spam(ctx, numero = 1):
  global second_admin
  global stop

  print("{0.author.mention}".format(ctx.message))
  print("{}".format(ctx.guild.id))
  print("{}".format(ctx.message.channel.id))

  await ctx.send(head_complete("{}".format(ctx.guild.id)))#'¡El rico spam viene!')
  if numero >= 50:
      numero = 50
  stop = False
  for i in range(numero):
    if stop==True:
      stop = False
      break
    await ctx.send(var_complete("{}".format(ctx.guild.id)))

@bot.command()
async def info(ctx):
  global embed
  await ctx.send(embed = embed)

@bot.command()
async def Info(ctx):
  await info(ctx)

@bot.command()
async def stop(ctx):
  global stop
  stop = True
  await ctx.send('stoped')

@bot.command()
async def Stop(ctx):
  await stop(ctx)

bot.remove_command('help')
@bot.command(pass_context = True)
async def help(ctx):
  embed = discord.Embed(color= discord.Color.red(),title= "Spam Bot Help",type= "rich",description= "Help for commands")
  embed.add_field(name='spam',value="spam [number of times] (max = 50) (send spam)", inline = False)
  embed.add_field(name='self spam',value="self spam [number of times] (max = 50) (send spam to private chat)", inline = False)
  embed.add_field(name='more/mas spam', value="more/mas spam (give 7 of spam", inline = False)
  embed.add_field(name="more/mas self spam", value = "more/mas self spam (send you spam to private message)", inline = False)
  embed.add_field(name='stop',value="stop (stop the actual spam)", inline = False)
  embed.add_field(name='config',value="config [set value (head, var, default, admin)] [value]", inline = False)
  embed.add_field(name='info',value="info (give info of the bot)", inline = False)
  embed.add_field(name='help',value="help (give you some help)", inline = False)
  await ctx.send(embed = embed)

@bot.command()
async def Help(ctx):
  await help(ctx)

@bot.command()
async def config_yo(ctx, arg = 'none', *, recived = "head/var"):
  global second_admin
  global coso
  coso = True
  print(commands.has_permissions(administrator=True))

  author = "{0.author.mention}".format(ctx.message)
  #print(bot.channel.id)
  #await ctx.send(author)
  print(recived)
  author2 = ''

  for i in author:
        if i == '!':
          pass
        else:
          author2 += i
  author = author2

  if author == "<@689534437356077184>" or author == second_admin:
    if arg == 'head':
      config_head("{}".format(ctx.guild.id), recived)
      await ctx.send('Right config')
    elif arg == 'var':
      config_var("{}".format(ctx.guild.id), recived)
      await ctx.send('Right config')
    elif arg == 'default':
      config_head("{}".format(ctx.guild.id),'¡El rico spam viene!')
      config_var("{}".format(ctx.guild.id),'El spam for you:\nhttps://www.youtube.com/channel/UCOiUjXdZ_kXJNXXjwtEsiQg')
      await ctx.send('Right config')
    elif arg == 'admin':
      for i in recived:
        if i == '!':
          pass
        else:
          second_admin += i
      #second_admin = recived
      print (second_admin)
      await ctx.send('Admin set')
    elif arg == 'none':
      await ctx.send('No arguments were given')
    else:
      await ctx.send('No reconible value')
  else:
    await ctx.send('You are not the admin')

@commands.has_permissions(manage_channels=True)
@bot.command(pass_context = True)
async def clear(ctx, number):
    mgs = [] #Empty list to put all the messages in the log
    number = int(number) #Converting the amount of messages to delete to an integer
    async for x in bot.logs_from(ctx.message.channel, limit = number):
        mgs.append(x)
    await bot.delete_messages(mgs)


@commands.has_permissions(administrator=True)
@bot.command()
async def config(ctx, arg = 'none', *, recived = "head/var"):
  global second_admin
  global coso
  coso = True
  print(commands.has_permissions(administrator=True))

  author = "{0.author.mention}".format(ctx.message)
  #print(bot.channel.id)
  #await ctx.send(author)
  print(recived)
  author2 = ''

  for i in author:
        if i == '!':
          pass
        else:
          author2 += i
  author = author2

  if author == "<@689534437356077184>" or author == second_admin or True:
    if arg == 'head':
      config_head("{}".format(ctx.guild.id), recived)
      await ctx.send('Right config')
    elif arg == 'var':
      config_var("{}".format(ctx.guild.id), recived)
      await ctx.send('Right config')
    elif arg == 'default':
      config_head("{}".format(ctx.guild.id),'¡El rico spam viene!')
      config_var("{}".format(ctx.guild.id),'El spam for you:\nhttps://www.youtube.com/channel/UCOiUjXdZ_kXJNXXjwtEsiQg')
      await ctx.send('Right config')
    elif arg == 'admin':
      for i in recived:
        if i == '!':
          pass
        else:
          second_admin += i
      #second_admin = recived
      print (second_admin)
      await ctx.send('Admin set')
    elif arg == 'none':
      await ctx.send('No arguments were given')
    else:
      await ctx.send('No reconible value')
  else:
    await ctx.send('You are not the admin')

@bot.command()
async def self(ctx, value = 'spam', value2 = 1):
  global stop

  if value2 >= 50:
    value2 = 50
  if value == 'spam':
    await ctx.author.send(head_complete("{}".format(ctx.guild.id)))
    stop = False
    for i in range(value2):
      if stop==True:
        stop = False
        break
      await ctx.author.send(var_complete("{}".format(ctx.guild.id)))

@bot.command()
async def case(ctx, user_id = '', *, dm):

  user_id2 = ''

  for i in user_id:
        if i == '!':
          pass
        else:
          user_id2 += i
  user_id = user_id2

  user = bot.get_user(user_id)
  bot.send_message(user, dm)

@bot.command()
async def send_dm(ctx, member: discord.Member, number = 1, *, content):
  global stop
  stop = False
  print(member.id)
  if number >= 100:
    number = 100
  channel = await member.create_dm()
  for i in range(number):
    if stop==True:
      stop = False
      break
    await channel.send(content)

@bot.command()
async def send_dm2(ctx, member, number = 1, *, content):
  global stop
  stop = False
  user = client.get_user(member)
  if number >= 100:
    number = 100
  for i in range(number):
    if stop==True:
      stop = False
      break
    await user.send('👀')

'''
@bot.command()
async def callate(ctx):
  global stop
  stop = False
  await ctx.send("no gracias")
  for i in range(100):
    if stop==True:
      stop = False
      break
    await ctx.send("suerte")
    '''

@bot.command()
async def more(ctx, value = 'spam', value2 = ''):

  if value == 'spam':
    await spam(ctx, 7)
  elif value == 'self' and value2 == 'spam':
    self('spam', 7)
  
  
@bot.command()
async def mas(ctx, value1 = 'spam', value2 = ''):
  await more(ctx, value1, value2)

@bot.command()
async def Mas(ctx, value1 = 'spam', value2 = ''):
  await more(ctx, value1, value2)

@bot.command()
async def More(ctx, value1 = 'spam', value2 = ''):
  await more(ctx, value1, value2)

token = os.environ.get("Token")
bot.run(token)
