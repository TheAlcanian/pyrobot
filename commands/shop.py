@bot.command()
async def shop(ctx):
  shopEmbed = discord.Embed(title="Shop", description="Buy something using `pr.buy ")

  shopEmbed.set_author(name="PyRobot", icon_url="https://cdn.discordapp.com/avatars/503024140706643968/6b57be03dc7ac21f337884fbbe4516de.webp")
  # embed.add_field(name="Voice Latency", value=str(VoiceClient.latency))
  shopEmbed.add_field(name="Text Latency", value=str(int(bot.latency * 1000)) + 'ms')

  await ctx.send(embed=shopEmbed)
