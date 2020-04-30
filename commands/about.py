@bot.command()
async def about(ctx):
  embed = discord.Embed(title="Credits", description="Who knows who built this tool anyways?")
  embed.set_author(name="PyRobot", icon_url="https://cdn.discordapp.com/avatars/503024140706643968/6b57be03dc7ac21f337884fbbe4516de.webp")
  embed.add_field(name="...The Shadow Knows!", value=('Credits to Shardion#4555 for making this bot\'s base, as well as all of the amazing contributors on GitHub!\nhttps://github.com/TheAlcanian/pyrobot'))

  await ctx.send(embed=embed)
