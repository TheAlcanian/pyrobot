@bot.command()
async def shop(ctx):
  shopEmbed = discord.Embed(title="Shop", description="Buy something using `pr.buy`")

  itemsfile = open("./items.json", 'r+')
  amounts = json.load(itemsfile)
  itemsfile.close()

# pr.register code for use
#  id = ctx.message.author.id
#  if str(id) not in amounts:
#    currencyfile = open('./currency.json', 'r+')
#    json.load(currencyfile)
#    amounts[id] = str("100")
#    json.dump(amounts, currencyfile)
#    await ctx.send(embed=successEmbed)
#    currencyfile.close()
#    currencyfile = open('./currency.json', 'r')
#    currencyfile.read()
#    currencyfile.close()
#  else:
#    await ctx.send(embed=failiureEmbed)


  
  shopEmbed.set_author(name="PyRobot", icon_url="https://cdn.discordapp.com/avatars/503024140706643968/6b57be03dc7ac21f337884fbbe4516de.webp")
  # embed.add_field(name="Voice Latency", value=str(VoiceClient.latency))
  for amount in amounts:
    shopEmbed.add_field(name='`' + amounts[amount]['actualname'] + '`', value=str(amounts[amount]['friendlyname']) + '\n' + amounts[amount]['description'] + '\nCosts: ' + amounts[amount]['cost'], inline='false')
    print('added ' + amounts[amount]['actualname'])
  
  await ctx.send(embed=shopEmbed)
