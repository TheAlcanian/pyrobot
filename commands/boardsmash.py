@bot.command()
async def boardsmash(ctx, *, arg):
  # make an embed
  embed = discord.Embed(title="Board Smashing", description="My protocols require " + ctx.message.mentions[0].mention + " to be... board smashed!")
  embed.set_author(name="PyRobot", icon_url="https://cdn.discordapp.com/embed/avatars/0.png")
  # send that embed with a file
  await ctx.send(embed=embed, file=discord.File('boardsmashing.png'))
