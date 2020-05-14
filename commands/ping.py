@bot.command()
async def ping(ctx):
  # make an embed
  embed = discord.Embed(title="Discord Latency", description="Time it takes to reach Discord's servers")

  embed.set_author(name="PyRobot", icon_url="https://cdn.discordapp.com/avatars/503024140706643968/6b57be03dc7ac21f337884fbbe4516de.webp")
  # embed.add_field(name="Voice Latency", value=str(VoiceClient.latency))
  # set this field's value to the current latency
  embed.add_field(name="Text Latency", value=str(int(bot.latency * 1000)) + 'ms')
  # send embed
  await ctx.send(embed=embed)
