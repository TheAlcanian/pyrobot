@bot.command(name='balance', aliases=['bal'], brief='Checks your PyRoll count', pass_ctx=True)
async def balance(ctx):
  # open currency file for reading, then get the JSON data from it and store that in a var, then close the currency file
  currencyfile = open('./currency.json', 'r')
  amounts = json.load(currencyfile)
  currencyfile.close()
  # success embed
  successEmbed = discord.Embed(title="PyRoll Bank", description="You have " + str(amounts[str(ctx.message.author.id)]) + " PyRolls!")
  # send success embed
  await ctx.send(embed=successEmbed)
