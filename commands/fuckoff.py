@bot.command()
async def fuckoff(ctx):
  # if the bot owner is running the command
  if await bot.is_owner(ctx.message.author):
    # embed
    embed = discord.Embed(title="Shutdown", description="Being the being of begone-ing")

    embed.set_author(name="PyRobot", icon_url="https://cdn.discordapp.com/avatars/503024140706643968/6b57be03dc7ac21f337884fbbe4516de.webp")
    # embed.add_field(name="Voice Latency", value=str(VoiceClient.latency))
    embed.add_field(name="Fucking off...", value='<:hahayes:707028764156100728>')

    # send embed
    await ctx.send(embed=embed)

 # inventoryfile.close()
 # currencyfile.
#    inventoryfile = open("./inventory.json", "w")
#    currencyfile = open("./currency.json", 'w')
#    json.dump(items, inventoryfile)
#    json.dump(amounts, currencyfile)
#    inventoryfile.close()
#    currencyfile.close()
    # die
    exit(0)
  # if the bot owner is not the person running the command
  else:
    # embed
    embed = discord.Embed(title="Shutdown", description="Being the being of begone-ing")

    embed.set_author(name="PyRobot", icon_url="https://cdn.discordapp.com/avatars/503024140706643968/6b57be03dc7ac21f337884fbbe4516de.webp")
    # embed.add_field(name="Voice Latency", value=str(VoiceClient.latency))
    embed.add_field(name="Error", value='You aren\'t allowed to tell me to fuck off!')
    # send embed
    await ctx.send(embed=embed)
