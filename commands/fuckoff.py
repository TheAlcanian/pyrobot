@bot.command()
async def fuckoff(ctx):
  embed = discord.Embed(title="Shutdown", description="Being the being of begone-ing")

  embed.set_author(name="PyRobot", icon_url="https://cdn.discordapp.com/avatars/503024140706643968/6b57be03dc7ac21f337884fbbe4516de.webp")
  # embed.add_field(name="Voice Latency", value=str(VoiceClient.latency))
  embed.add_field(name="Fucking off...", value='<:hahayes:694385453624721438>')

  await ctx.send(embed=embed)
  currencyfile = open("./currency.json", 'r+')
  json.dump(amounts, currencyfile)
  currencyfile.close()
  exit(0)