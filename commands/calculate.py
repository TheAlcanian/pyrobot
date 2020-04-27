from discord.ext import commands
import discord
import random

@bot.command()
async def calculate(ctx, arg1, arg2, arg3):
  async def embedcalc(num1, modifier, num2):
    responders = ['Spy', 'Sniper', 'Pyro', 'Heavy', 'Engineer', 'Soldier', 'Demoman', 'Scout', 'Medic', 'Jevil', 'TCG', 'CK', 'Double-T', 'ROFL', 'urnotzach']

    calculation = '0'

    if arg2 + arg3 == "/0":
      errorEmbed = discord.Embed(title="Error", description="Uh-oh! PyRobot encountered an error!", colour=discord.Colour(0xe04c4c))
      errorEmbed.set_author(name="PyRobot", url="https://discordapp.com", icon_url="https://cdn.discordapp.com/avatars/503024140706643968/6b57be03dc7ac21f337884fbbe4516de.webp")
      errorEmbed.add_field(name="Error Description", value="Cannot divide by 0.")
      await ctx.send(embed=errorEmbed)
      return
      
    if modifier == '+':
      calculation = str(int(num1) + int(num2))
    if modifier == '-':
      calculation = str(int(num1) - int(num2))
    if modifier == '*':
      calculation = str(int(num1) * int(num2))
    if modifier == '/':
      calculation = str(int(num1) / int(num2))
    
    embed = discord.Embed(title="Calculate", description="I asked **" + random.choice(responders) + "** about your formula and they said...")

    embed.set_author(name="PyRobot", url="https://discordapp.com", icon_url="https://cdn.discordapp.com/avatars/503024140706643968/6b57be03dc7ac21f337884fbbe4516de.webp")

    embed.add_field(name="Formula", value=num1 + ' ' + modifier + ' ' + num2, inline=True)
    embed.add_field(name="Result", value=calculation, inline=True)

    await ctx.send(embed=embed)
                        
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
