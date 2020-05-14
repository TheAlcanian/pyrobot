@bot.command(name='register', aliases=['reg'], brief='Registers your account', pass_ctx=True)
async def register(ctx):
  # embed if nothing bad happens
  successEmbed = discord.Embed(title="PyRoll Bank", description="Register an account at the PyRoll Bank")

  successEmbed.set_author(name="PyRobot", icon_url="https://cdn.discordapp.com/avatars/503024140706643968/6b57be03dc7ac21f337884fbbe4516de.webp")
  # embed.add_field(name="Voice Latency", value=str(VoiceClient.latency))
  successEmbed.add_field(name="Success!", value='Your account has been registered!')

  # embed if something bad happens
  failiureEmbed = discord.Embed(title="PyRoll Bank", description="Register an account at the PyRoll Bank")

  failiureEmbed.set_author(name="PyRobot", icon_url="https://cdn.discordapp.com/avatars/503024140706643968/6b57be03dc7ac21f337884fbbe4516de.webp")
      # embed.add_field(name="Voice Latency", value=str(VoiceClient.latency))
  failiureEmbed.add_field(name="Failiure...", value='You already have an account!')

  # shorthand for user's id
  id = ctx.message.author.id
  # open both inventory file and currency file, put the JSON data in a var, then close both
  inventoryfile = open('./inventory.json', 'r+')
  currencyfile = open('./currency.json', 'r+')
  amounts = json.load(currencyfile)
  items = json.load(inventoryfile)
  inventoryfile.close()
  currencyfile.close()
  # if the user is not in the currency file
  if str(id) not in amounts:
    # open currency file as overwrite with updating
    currencyfile = open('./currency.json', 'w+')
    # debugging
    print(amounts)
    print('STHAP')
    # add them to the currency file with 100 pyrolls to start
    amounts[id] = str("100")
    # dump the amounts var to the currency file
    json.dump(amounts, currencyfile)
    # send the success embed
    await ctx.send(embed=successEmbed)
    # close currency file
    currencyfile.close()
  # if the user is not in the inventory file
  if str(id) not in items:
    # open inventory file as overwrite with updating
    inventoryfile = open('./inventory.json', 'w+')
    # give them some test items to start (they dont exist in inventory.json yet)
    items[id] = ['item', 'item2']
    # dump the items var to the inventory file
    json.dump(items, inventoryfile)
    # send the success embed
    # TODO: make this not send twice if both currency and inventory are added for the user?
    await ctx.send(embed=successEmbed)

  # if the user... why the fuck does this work?
  # if the user isnt in inventory or currency file
  else:
    if str(id) not in amounts or items:
      # debugging
      print(amounts)
      # send fail embed
      await ctx.send(embed=failiureEmbed)
      # close inventory and currency files
      currencyfile.close()
      inventoryfile.close()
