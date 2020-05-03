@bot.command(name='register', aliases=['reg'], brief='Registers your account', pass_ctx=True)
async def register(ctx):

  successEmbed = discord.Embed(title="PyRoll Bank", description="Register an account at the PyRoll Bank")

  successEmbed.set_author(name="PyRobot", icon_url="https://cdn.discordapp.com/avatars/503024140706643968/6b57be03dc7ac21f337884fbbe4516de.webp")
  # embed.add_field(name="Voice Latency", value=str(VoiceClient.latency))
  successEmbed.add_field(name="Success!", value='Your account has been registered!')

  failiureEmbed = discord.Embed(title="PyRoll Bank", description="Register an account at the PyRoll Bank")

  failiureEmbed.set_author(name="PyRobot", icon_url="https://cdn.discordapp.com/avatars/503024140706643968/6b57be03dc7ac21f337884fbbe4516de.webp")
      # embed.add_field(name="Voice Latency", value=str(VoiceClient.latency))
  failiureEmbed.add_field(name="Failiure...", value='You already have an account!')

  id = ctx.message.author.id
  currencyfile = open('./currency.json', 'r+')
  amounts = json.load(currencyfile)
  currencyfile.close()
  if str(id) not in amounts:
    currencyfile = open('./currency.json', 'w+')
    print(amounts)
    amounts[id] = str("100")
    json.dump(amounts, currencyfile)
    await ctx.send(embed=successEmbed)
    currencyfile.close()

    #debugging
    currencyfile = open('./currency.json', 'r')
    currencyfile.read()
    currencyfile.close()
  else:
    print(amounts)
    await ctx.send(embed=failiureEmbed)
    currencyfile.close()
