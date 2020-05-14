@bot.command()
async def shop(ctx):
  shopEmbed = discord.Embed(title="Shop", description="Buy something using `pr.buy`")
  # open inventory file as read with updating
  # TODO: why cant we just open as read? can we?
  itemsfile = open("./items.json", 'r+')
  # read out JSON data into a var
  amounts = json.load(itemsfile)
  # kill. the inventory file
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


  # shop embed
  shopEmbed.set_author(name="PyRobot", icon_url="https://cdn.discordapp.com/avatars/503024140706643968/6b57be03dc7ac21f337884fbbe4516de.webp")
  # iterate over every item in the inventory file
  # TODO: why are we using the same value as the currency file for this? i should change that
  for amount in amounts:
    # add item to the embed
    shopEmbed.add_field(name='`' + amounts[amount]['actualname'] + '`', value=str(amounts[amount]['friendlyname']) + '\n' + amounts[amount]['description'] + '\nCosts: ' + amounts[amount]['cost'], inline='false')
    print('added ' + amounts[amount]['actualname'])
  # send embed
  await ctx.send(embed=shopEmbed)
