@bot.command(name='balance', aliases=['bal'], brief='Checks your PyRoll count', pass_ctx=True)
async def balance(ctx):
  # open currency file for reading, then get the JSON data from it and store that in a var, then close the currency file
  currencyfile = open('./currency.json', 'r')
  amounts = json.load(currencyfile)
  currencyfile.close()
  # success embed
  successEmbed = discord.Embed(title="PyRoll Bank", description="You have " + str(amounts[str(ctx.message.author.id)]) + " PyRolls!")
  successEmbed.set_author(name="PyRobot", icon_url="https://cdn.discordapp.com/avatars/503024140706643968/6b57be03dc7ac21f337884fbbe4516de.webp")
  # send success embed
  await ctx.send(embed=successEmbed)
