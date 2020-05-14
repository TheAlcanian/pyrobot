from discord.ext import commands
import discord
import random

@bot.command()
async def calculate(ctx, arg1, arg2, arg3):
  async def embedcalc(num1, modifier, num2):
    # list of characters that can respond
    responders = ['Spy', 'Sniper', 'Pyro', 'Heavy', 'Engineer', 'Soldier', 'Demoman', 'Scout', 'Medic']

    # define calculation here for some reason lol
    calculation = '0'

    # if user tries to divide by zero, send a special embed
    if arg2 + arg3 == "/0":
      errorEmbed = discord.Embed(title="Error", description="Uh-oh! PyRobot encountered an error!", colour=discord.Colour(0xe04c4c))
      errorEmbed.set_author(name="PyRobot", url="https://discordapp.com", icon_url="https://cdn.discordapp.com/avatars/503024140706643968/6b57be03dc7ac21f337884fbbe4516de.webp")
      errorEmbed.add_field(name="Error Description", value="Cannot divide by 0.")
      await ctx.send(embed=errorEmbed)
      return

    # bad code
    # if the modifier is +, add the two numbers together
    if modifier == '+':
      calculation = str(int(num1) + int(num2))
    # if the modifier is -, subtract the number on the left with the number on the right
    if modifier == '-':
      calculation = str(int(num1) - int(num2))
    # if the modifier is *, multiply the number on the left by the number on the right
    if modifier == '*':
      calculation = str(int(num1) * int(num2))
    # if the modifier is /, divide the number on the left by the number on the right
    if modifier == '/':
      calculation = str(int(num1) / int(num2))

    # embed
    embed = discord.Embed(title="Calculate", description="I asked **" + random.choice(responders) + "** about your formula and they said...")

    embed.set_author(name="PyRobot", url="https://discordapp.com", icon_url="https://cdn.discordapp.com/avatars/503024140706643968/6b57be03dc7ac21f337884fbbe4516de.webp")

    embed.add_field(name="Formula", value=num1 + ' ' + modifier + ' ' + num2, inline=True)
    embed.add_field(name="Result", value=calculation, inline=True)

    # send embed
    await ctx.send(embed=embed)
  # why did I put that into a function? oh well
  # *actually* sends the embed
  await embedcalc(arg1, arg2, arg3)
#      if arg2 == '+':    
#        await ctx.send('I asked **' + random.choice(responders) + '** what **' + arg1 + ' + ' + arg3 + '** is and they said **' + str(int(arg1) + int(arg3)) + '**.')
#
#      if arg2 == '-':
#        await ctx.send('I asked **' + random.choice(responders) + '** what **' + arg1 + ' - ' + arg3 + '** is and they said **' + str(int(arg1) - int(arg3)) + '**.')
#
#      if arg2 == '*':
#        await ctx.send('I asked **' + random.choice(responders) + '** what **' + arg1 + ' * ' + arg3 + '** is and they said **' + str(int(arg1) * int(arg3))  + '**.')
#
#      if arg2 == '/':
#        await ctx.send('I asked **' + random.choice(responders) + '** what **' + arg1 + ' / ' + arg3 + '** is and they said **' + str(int(arg1) / int(arg3)) + '**.')
