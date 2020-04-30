@bot.command(name='balance', aliases=['bal'], brief='Checks your PyRoll count', pass_ctx=True)
async def balance(ctx):
  successEmbed = discord.Embed(title="PyRoll Bank", description="You have " + amounts[str(ctx.message.author.id)] + " PyRolls!")
  await ctx.send(embed=successEmbed)
